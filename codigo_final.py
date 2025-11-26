from typing import List, Optional
import re

class CodigoFinal:
    def __init__(self, tac_linhas: List[str]):
        self.tac = [l.strip() for l in tac_linhas if l and l.strip()]
        self.rotulos = {}
        self._mapear_rotulos()
        self.out_lines = []
        self.indent = 0

    # localiza todas as labels do TAC
    def _mapear_rotulos(self):
        for idx, linha in enumerate(self.tac):
            if linha.endswith(":"):
                self.rotulos[linha[:-1]] = idx

    # Emite uma linha de saída formatada
    def _emitir(self, texto=""):
        self.out_lines.append("    " * self.indent + texto)

    # Gera o arquivo final em Python
    def gerar(self) -> str:
        self._emitir("def main():")
        self.indent += 1

        # processa uma linha do tac 
        i = 0
        while i < len(self.tac):
            i = self._processar_linha(i)

        # Gera a chamada final de maneira correta
        self.indent = 0 # 0 funcionou
        self._emitir("")
        self._emitir("if __name__ == '__main__':")
        self._emitir("    main()")
        return "\n".join(self.out_lines)

    # Processa uma linha do TAC
    def _processar_linha(self, i: int) -> int:
        linha = self.tac[i]

        #declaração
        if linha.startswith("decl "):
            self._emitir(f"{linha.split()[1]} = 0")
            return i + 1

        #input 
        if linha.startswith("read "):
            self._emitir(f"{linha.split()[1]} = float(input())") #usando float pra não dar problema
            return i + 1
        
        #print 
        if linha.startswith("print("):
            m = re.match(r'print\(\s*"[^"]+"\s*,\s*(.+)\)', linha)
            if m:
                self._emitir(f"print({m.group(1).strip()})")
            else:
                self._emitir(linha)
            return i + 1
        
        # while (procura por uma label)
        if linha.endswith(":"): # detecta se é label
            label = linha[:-1]
            back = self._buscar_retorno(label) # verifica se possui um salto pra essa label 
            if back is not None: # se não possuir avança 
                idx_if = self._buscar_if_proximo(self.rotulos[label], 3) # se possuir procura um if e extrai a condição
                if idx_if is not None:
                    cond = self._extrair_condicao(self.tac[idx_if])
                    self._emitir(f"while {cond}:")
                    self.indent += 1
                    
                    # gera o conteudo do while e procura o goto para encerrar o loop
                    j = idx_if + 1
                    while j < len(self.tac):
                        if self.tac[j].startswith("goto ") and self.tac[j].split()[1] == label:
                            destino = self._destino_do_if(self.tac[idx_if])
                            fim = self.rotulos.get(destino, j + 1)
                            self.indent -= 1
                            return fim + 1
                        j = self._processar_intervalo(j, parar_em={label})

                    self.indent -= 1
                    return j
            return i + 1

        #if 
        if linha.startswith("if "):
            
            if " goto " not in linha: # #if sem else detecta que não possui um goto
                cond = self._extrair_condicao(linha)
                self._emitir(f"if {cond}:")
                self.indent += 1
                return i + 1

            
            destino_else = self._destino_do_if(linha) #detecta a label do else 
            proximo_goto = self._buscar_proximo_goto(i + 1) 

            if proximo_goto is not None:
                destino_fim = self.tac[proximo_goto].split()[1]

                if destino_else in self.rotulos and destino_fim in self.rotulos:
                    if self.rotulos[destino_else] < self.rotulos[destino_fim]:

                        cond = self._extrair_condicao(linha)
                        self._emitir(f"if {cond}:")
                        self.indent += 1
                        
                        # Processa bloco THEN (entre o if e o goto)
                        k = i + 1
                        while k < proximo_goto:
                            k = self._processar_linha(k)
                        self.indent -= 1

                        self._emitir("else:")
                        self.indent += 1

                        k = self.rotulos[destino_else] + 1
                        while k < self.rotulos[destino_fim]:
                            k = self._processar_linha(k)
                        self.indent -= 1

                        return self.rotulos[destino_fim] + 1

            cond = self._extrair_condicao(linha)
            self._emitir(f"if {cond}:")
            self.indent += 1
            return i + 1

        if linha.startswith("goto "):
            return i + 1

        if "=" in linha:
            linha_py = re.sub(r'\s+', ' ', linha.replace("||", "or").replace("&&", "and"))
            self._emitir(linha_py)
            return i + 1

        return i + 1

    # Processa um bloco até encontrar labels de parada
    def _processar_intervalo(self, start_idx: int, parar_em=set()) -> int:
        j = start_idx
        while j < len(self.tac):
            if self.tac[j].endswith(":") and self.tac[j][:-1] in parar_em:
                break
            j = self._processar_linha(j)
        return j

    # Procura goto de retorno (loop)
    def _buscar_retorno(self, label: str) -> Optional[int]:
        for idx in range(self.rotulos.get(label, -1) + 1, len(self.tac)):
            if self.tac[idx].startswith("goto ") and self.tac[idx].split()[1] == label:
                return idx
        return None

    # procura um if (condição do while)
    def _buscar_if_proximo(self, idx_label: int, alcance: int) -> Optional[int]:
        for k in range(idx_label + 1, min(idx_label + 1 + alcance, len(self.tac))):
            if self.tac[k].startswith("if "):
                return k
        return None

    # procura o proximo goto (encontra o fim de um if)
    def _buscar_proximo_goto(self, start_idx: int) -> Optional[int]:
        for j in range(start_idx, len(self.tac)):
            if self.tac[j].startswith("goto "):
                return j
        return None

    # converte as condições do TAC para pyhton (resolve as condições e remore as labels)
    def _extrair_condicao(self, linha_if: str) -> str:
        s = linha_if.strip()[3:]
        left = s.split(" goto ")[0].strip() if " goto " in s else s

        m = re.match(r'(.+?)\s*==\s*0$', left)
        if m:
            return self._resolver_temp(m.group(1).strip())

        if re.search(r'(<=|>=|==|!=|<|>)', left):
            return left

        return left
    
    # bloco apos o um fi 
    def _destino_do_if(self, linha_if: str) -> str:
        return linha_if.split(" goto ")[1].strip()
    
    #transforma as var temporarias nas originais (t1 vira a condição original)
    def _resolver_temp(self, temp: str) -> str:
        for linha in self.tac:
            if linha.startswith(temp + " ="):
                rhs = linha.split("=", 1)[1].strip()
                rhs = re.sub(r'\s+', ' ', rhs).replace("||", "or").replace("&&", "and")
                return rhs
        return temp
