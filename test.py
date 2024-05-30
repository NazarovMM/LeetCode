nums1 = [1, 2]
nums2 = [3, 4]

len1 = len(nums1)
len2 = len(nums2)
output = []
i = 0
j = 0
flag1 = True
flag2 = True
while len(output) < (len1+len2):
    if nums1[i] <= nums2[j] and flag1:
        output.append(nums1[i])
        if i < len1-1:
            i += 1
        else:
            flag1 = False
    elif nums2[j] <= nums1[i] and flag2:
        output.append(nums2[j])
        if j < len2-1:
            j += 1
        else:
            flag2 = False
    elif flag1 and flag2 == False:
        output.append(nums1[i])
        if i < len1-1:
            i += 1
        else:
            flag1 = False
    else:
        output.append(nums2[j])
        if j < len2-1:
            j += 1
        else:
            flag2 = False

if len(output)//2 == 1:
    pass #print(output[int(len(output)/2)-1])
else:
    pass #print((output[int(len(output)/2)-1]+output[int(len(output)/2)])/2)

