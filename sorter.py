# ---- ---- ---- ----
def sorter(array):
    tmp = []
    for i in range(len(array)):
        val = 0
        for j in range(len(tmp)):
            if array[i] < tmp[j]:
                val = []
                # ---- ---- ---- ----
                #tmp.insert(j, array[i])
                # Same as above, but manually
                for k in range(j):
                    val.append(tmp[k])
                val.append(array[i])
                for k in range(j, len(tmp)):
                    val.append(tmp[k])
                # ---- ---- ---- ----
                tmp = val
                break
        # If current number is bigger than all previous
        if val == 0:
            tmp.append(array[i])
    return tmp
# ---- ---- ---- ----

print(sorter([94, 58, 47, 44, 45, 21, 92, 90, 91, 76]))
input()
