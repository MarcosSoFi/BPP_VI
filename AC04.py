
import pdb
pdb.set_trace()


def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo


#   [1.1] List Comprehension
#	----------------------------------------------------------------
# 	List Comprehension
nums 	 = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
max_num1 = [max(i) for i in nums]

# 	Loop
max_num2 = []
for i in nums:
	max_num2.append(max(i))

print("Max Values - List Comprehension\n", max_num1)
print("Max Values - Loop\n",max_num2)


#   [1.2] Filter
#	----------------------------------------------------------------
lst   		= [3, 4, 8, 5, 5, 22, 13]

prime_nums1 = list(filter(es_primo, lst))

prime_nums2 = [i for i in lst if es_primo(i)]

prime_nums3 = []
for i in lst:
    if es_primo(i):
        prime_nums3.append(i)

print("Prime Numbers1 - Filter\n", prime_nums1)
print("Prime Numbers2 - List Comprehension\n", prime_nums2)
print("Prime Numbers3 - Loop\n", prime_nums3)




