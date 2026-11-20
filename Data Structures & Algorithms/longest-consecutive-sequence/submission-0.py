class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        ordenados = sorted(nums)
        seen = set()
        racha_actual = 1
        max_resultado = 1
        
        for i in range(len(ordenados) - 1):
            # Si es duplicado, lo saltamos sin romper la racha
            if ordenados[i + 1] == ordenados[i]:
                continue
                
            if (ordenados[i + 1] - ordenados[i]) == 1 and ordenados[i] not in seen:
                racha_actual += 1
                seen.add(ordenados[i])
                max_resultado = max(max_resultado, racha_actual)
            else:
                # Si la diferencia es > 1, se rompe la secuencia y reiniciamos
                racha_actual = 1

        return max_resultado

        