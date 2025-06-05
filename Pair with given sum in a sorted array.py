class Solution:
    def countPairs(self, arr, target): 
        n = len(arr)
        left = 0
        right = n - 1
        count = 0

        while left < right:
            current_sum = arr[left] + arr[right]

            if current_sum == target:
                # Agar dono elements same hain, toh combination ka formula lagaao
                if arr[left] == arr[right]:
                    length = right - left + 1
                    count += (length * (length - 1)) // 2
                    break
                else:
                    l_val = arr[left]
                    r_val = arr[right]
                    l_count = 0
                    r_count = 0

                    # Left side ke duplicates count karo
                    while left < right and arr[left] == l_val:
                        l_count += 1
                        left += 1

                    # Right side ke duplicates count karo
                    while right >= left and arr[right] == r_val:
                        r_count += 1
                        right -= 1

                    # Pair count = left count * right count
                    count += l_count * r_count

            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return count
