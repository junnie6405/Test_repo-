def min_roof_length(parking_spots, k):
    if not parking_spots or k == 0:
        return 0
    if k > len(parking_spots): return None

    parking_spots.sort()
    ans = float('inf')
    for i in range(len(parking_spots) - k + 1):
        ans = min(ans, parking_spots[k-1+i] - parking_spots[i] + 1)

    return ans 

parking_spots = [5,6,9,12,2]
k = 4

ans = min_roof_length(parking_spots, k)
print(ans)



