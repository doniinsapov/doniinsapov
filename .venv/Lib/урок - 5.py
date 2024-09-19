from примеры import my_list

x = ['Pasha', 'Misha', 'Jordan', 'Mike']
y = []
for imena in x:
    if 'a' in imena:
        y.append(imena)
print(y) #['Pasha', 'Misha', 'Jordan']

numbers = [i for i in range(1, 100)]
print(numbers) # ot 1 po 99


numes = [1, 2, 3, 4]
numbers2 = [spam*2 for spam in numes]
print(numbers2) # [2, 4, 6, 8]

names = 'Pasha'
n = []
for item in names:
    n.append(item)
print(n) # ['P', 'a', 's', 'h', 'a']

names = 'Pasha'
n =[x for x in names]
print(n) # ['P', 'a', 's', 'h', 'a']

nums = []
for i in range(100):
    nums.append(i)
print(nums) # ot 1 po 99

nums =[i for i in range(100)]
print(nums) # ot 1 po 99

nums = [i for i in range(100)]
print(nums) # ot 1 po 99

my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + '2' for i in my]
print(my2[1:3]) # ['332', 'Jordan2']

my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + '2' for i in my]
print(my2[-1]) # Pavel2

nums = [i for i in range(1, 11)]
chotnie = [num for num in nums if num % 2 == 0]
nechotnie = [num for num in nums if num % 2 != 0]
print(chotnie, nechotnie) # [2, 4, 6, 8, 10] [1, 3, 5, 7, 9]

names = ['Pavel', 'Jordan', 'Sasha']
names2 = []
for name in names:
    if 'o' in name:
        names2.append(name)
print(names2) # ['Jordan']

names = ['Pavel', 'Jordan', 'Sasha']
names2 = [name for name in names if 'o' in name]
print(names2) # ['Jordan']

my = ['2', '33', 'Jordan', 'Pavel']
my2 = [i + '2' for  i in my if 'a' in i]
print(my2) # ['Jordan2', 'Pavel2']

my_list = [i for i in range(1, 11, 2)]
print(my_list) # [1, 3, 5, 7, 9]

names = ['Pavel', 'Sasha', 'Jordan', 'Sasha']
answer = [i[0] for i in names]
print(answer) #['P', 'S', 'J', 'S']

nums = [1, 2, 3]
my_list = [i for i in range(1, 11) if i in nums]
print(my_list) # [1, 2, 3]

nums = [i for i in range(1, 21)]
print(nums) # ot 1 po 20

nums = [i for i in range(1, 21)]
chotnie = [num for num in nums if num % 2 == 0]
print(chotnie)# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

nums1 = [i for i in range(1, 21)]
nums2 = [e for e in nums1 if e % 2 == 0]
print(nums2) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


N = 5
a = [x ** 2 for x in range(N)]
print(a) # [0, 1, 4, 9, 16]

a = [x % 2 == 0 for x in range(N)]
print(a) # [True, False, True, False, True]

a = [0.5 * x + 1 for x in range(N)]
print(a) # [1.0, 1.5, 2.0, 2.5, 3.0]


a = [d for d in 'Programist']
print(a) # ['P', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 's', 't']

a = [x for x in range(-5, 5) if x < 0]
print(a) # [-5, -4, -3, -2, -1]

d_inp = input('Целые числа через пробел:')
a = [int(d) for d in d_inp.split()]
print(a) # Целые числа через пробел: 2 3 4 5 #[2, 3, 4, 5]