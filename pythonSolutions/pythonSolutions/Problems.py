import math
from functools import reduce

from pythonSolutions import Util

"""
If we list all the natural numbers below10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def question_1() -> int:
    list_numbs = []

    for i in range(1, 1000):
        if i % 3 == 0 and i % 5 == 0:
            list_numbs.append(i)
        elif i % 3 == 0:
            list_numbs.append(i)
        elif i % 5 == 0:
            list_numbs.append(i)

    return sum(list_numbs)


"""
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
"""


def problem_2() -> int:
    last = 1
    last_2 = 1

    sums = []

    while last < 4000000:
        fib = last + last_2

        last = last_2
        last_2 = fib

        if fib % 2 == 0:
            sums.append(fib)

    return sum(sums)


"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def problem_3() -> int:
    target = 600851475143
    upper_bound = int(math.sqrt(target))

    highest = 0

    for i in range(1, upper_bound):
        if target % i == 0:
            if Util.Util.is_prime(i):
                highest = i

    return highest


"""
A palindromic number reads the same both ways. The largest
palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.
"""


def problem_4() -> int:
    highest = 0

    for i in range(100, 999):
        for j in range(100, 999):
            prod = i * j
            if Util.Util.is_pal(prod):
                if prod > highest:
                    highest = prod

    return highest


"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def problem_5() -> int:
    primes = (2, 11, 13, 17, 19)

    initial = 2520

    for prime in primes:
        initial *= prime

    return initial


def problem_6() -> float:
    target = 100

    sum_of_squares = 0

    for i in range(1, target + 1):
        sum_of_squares += (i * i)

    sum_of_numbers = (target * (target + 1)) / 2

    return (sum_of_numbers * sum_of_numbers) - sum_of_squares


def problem_7() -> int:
    numb = 0
    target = 10001

    for i in range(2, 1000000):
        if Util.Util.is_prime(i):
            numb += 1
            if numb == target:
                return i


def problem_8() -> int:
    num = 0  # Number omitted as is 1000 digits.

    prod = 1
    max_prod = 0

    num_str = str(num)

    length = len(num_str)

    for i in range(1, length - 13 + 1):
        prod = 1
        for j in range(i, i + 13):
            prod *= int(num_str[j - 1: j])

            if prod > max_prod:
                max_prod = prod

    return max_prod


def problem_11():

    grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8], [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0], [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65], [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91], [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80], [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50], [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70], [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21], [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72], [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95], [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92], [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57], [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58], [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40], [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66], [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69], [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36], [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16], [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54], [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
    grid_size = 20

    max_prod = -1

    for y in range(0, grid_size):
        y_row = grid[y]

        for x in range(0, grid_size):
            if (x + 3) < grid_size:
                prod = reduce(lambda a, b: a * b, y_row[x:x + 4])
                if prod > max_prod:
                    max_prod = prod

        if (y + 3) < grid_size:
            ks = grid[y: y + 4]

            for x2 in range(0, grid_size):
                prod = 1
                for row in ks:
                    prod *= row[x2]

                if prod > max_prod:
                    max_prod = prod

        for i in range(0, grid_size):
            tmp = []
            for x in range(0, 4):
                if i + x < 19:
                    tmp.append(grid[x][i+x])
            if len(tmp) > 3:
                print(tmp)
                prod = reduce(lambda a, b: a * b, tmp)
                if prod > max_prod:
                    max_prod = prod





    return max_prod


def problem_13() -> int:
    numb = (37107287533902102798797998220837590246510135740250,
            46376937677490009712648124896970078050417018260538,
            74324986199524741059474233309513058123726617309629,
            91942213363574161572522430563301811072406154908250,
            23067588207539346171171980310421047513778063246676,
            89261670696623633820136378418383684178734361726757,
            28112879812849979408065481931592621691275889832738,
            44274228917432520321923589422876796487670272189318,
            47451445736001306439091167216856844588711603153276,
            70386486105843025439939619828917593665686757934951,
            62176457141856560629502157223196586755079324193331,
            64906352462741904929101432445813822663347944758178,
            92575867718337217661963751590579239728245598838407,
            58203565325359399008402633568948830189458628227828,
            80181199384826282014278194139940567587151170094390,
            35398664372827112653829987240784473053190104293586,
            86515506006295864861532075273371959191420517255829,
            71693888707715466499115593487603532921714970056938,
            54370070576826684624621495650076471787294438377604,
            53282654108756828443191190634694037855217779295145,
            36123272525000296071075082563815656710885258350721,
            45876576172410976447339110607218265236877223636045,
            17423706905851860660448207621209813287860733969412,
            81142660418086830619328460811191061556940512689692,
            51934325451728388641918047049293215058642563049483,
            62467221648435076201727918039944693004732956340691,
            15732444386908125794514089057706229429197107928209,
            55037687525678773091862540744969844508330393682126,
            18336384825330154686196124348767681297534375946515,
            80386287592878490201521685554828717201219257766954,
            78182833757993103614740356856449095527097864797581,
            16726320100436897842553539920931837441497806860984,
            48403098129077791799088218795327364475675590848030,
            87086987551392711854517078544161852424320693150332,
            59959406895756536782107074926966537676326235447210,
            69793950679652694742597709739166693763042633987085,
            41052684708299085211399427365734116182760315001271,
            65378607361501080857009149939512557028198746004375,
            35829035317434717326932123578154982629742552737307,
            94953759765105305946966067683156574377167401875275,
            88902802571733229619176668713819931811048770190271,
            25267680276078003013678680992525463401061632866526,
            36270218540497705585629946580636237993140746255962,
            24074486908231174977792365466257246923322810917141,
            91430288197103288597806669760892938638285025333403,
            34413065578016127815921815005561868836468420090470,
            23053081172816430487623791969842487255036638784583,
            11487696932154902810424020138335124462181441773470,
            63783299490636259666498587618221225225512486764533,
            67720186971698544312419572409913959008952310058822,
            95548255300263520781532296796249481641953868218774,
            76085327132285723110424803456124867697064507995236,
            37774242535411291684276865538926205024910326572967,
            23701913275725675285653248258265463092207058596522,
            29798860272258331913126375147341994889534765745501,
            18495701454879288984856827726077713721403798879715,
            38298203783031473527721580348144513491373226651381,
            34829543829199918180278916522431027392251122869539,
            40957953066405232632538044100059654939159879593635,
            29746152185502371307642255121183693803580388584903,
            41698116222072977186158236678424689157993532961922,
            62467957194401269043877107275048102390895523597457,
            23189706772547915061505504953922979530901129967519,
            86188088225875314529584099251203829009407770775672,
            11306739708304724483816533873502340845647058077308,
            82959174767140363198008187129011875491310547126581,
            97623331044818386269515456334926366572897563400500,
            42846280183517070527831839425882145521227251250327,
            55121603546981200581762165212827652751691296897789,
            32238195734329339946437501907836945765883352399886,
            75506164965184775180738168837861091527357929701337,
            62177842752192623401942399639168044983993173312731,
            32924185707147349566916674687634660915035914677504,
            99518671430235219628894890102423325116913619626622,
            73267460800591547471830798392868535206946944540724,
            76841822524674417161514036427982273348055556214818,
            97142617910342598647204516893989422179826088076852,
            87783646182799346313767754307809363333018982642090,
            10848802521674670883215120185883543223812876952786,
            71329612474782464538636993009049310363619763878039,
            62184073572399794223406235393808339651327408011116,
            66627891981488087797941876876144230030984490851411,
            60661826293682836764744779239180335110989069790714,
            85786944089552990653640447425576083659976645795096,
            66024396409905389607120198219976047599490197230297,
            64913982680032973156037120041377903785566085089252,
            16730939319872750275468906903707539413042652315011,
            94809377245048795150954100921645863754710598436791,
            78639167021187492431995700641917969777599028300699,
            15368713711936614952811305876380278410754449733078,
            40789923115535562561142322423255033685442488917353,
            44889911501440648020369068063960672322193204149535,
            41503128880339536053299340368006977710650566631954,
            81234880673210146739058568557934581403627822703280,
            82616570773948327592232845941706525094512325230608,
            22918802058777319719839450180888072429661980811197,
            77158542502016545090413245809786882778948721859617,
            72107838435069186155435662884062257473692284509516,
            20849603980134001723930671666823555245252804609722,
            53503534226472524250874054075591789781264330331690)

    full_numb = str(sum(numb))

    return int(full_numb[0:10])


def problem_16() -> int:
    numb = 2 ** 1000

    numb = str(numb)

    t_sum = 0
    for sub_str in numb:
        t_sum += int(sub_str)

    return t_sum


def problem_17() -> int:
    letters = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4}


def problem_18() -> int:
    row1 = (1,)
    row2 = (95, 64)
    row3 = (17, 47, 82)
    row4 = (18, 35, 87, 10)
    row5 = (20, 4, 82, 47, 65)
    row6 = (19, 1, 23, 75, 3, 34)
    row7 = (88, 2, 77, 73, 7, 63, 67)
    row8 = (99, 65, 4, 28, 6, 16, 70, 92)
    row9 = (41, 41, 26, 56, 83, 40, 80, 70, 33)
    row10 = (41, 48, 72, 33, 47, 32, 37, 16, 94, 29)
    row11 = (53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14)
    row12 = (70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57)
    row13 = (91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48)
    row14 = (63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31)
    row15 = (4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23)

    highest = 0

    for i in row2:
        total = 1


def problem_20() -> int:
    target = 100

    total_fact = math.factorial(target)
    fact_str = str(total_fact)

    return sum((int(x) for x in fact_str))


def problem_25() -> int:
    last = 1
    last_2 = 1

    count = 2
    while True:
        fib = last + last_2

        last = last_2
        last_2 = fib
        count += 1

        fib_str = str(fib)

        if len(fib_str) >= 1000:
            return count



def problem_26():
    longest = -1
    num = -1

    for i in range(3, 1001, 2):
        if i % 5 == 0:
            continue

        p = 1
        while (10 ** p) % i != 1:
            p += 1

        if p > longest:
            longest = p
            num = i

    print(num, longest)


def problem_30() -> int:
    sum_total = 0

    for i in range(2, 1000000):
        num_str = str(i)

        num_total = 0

        for j in num_str:
            int_digit = int(j)
            num_total += (int_digit ** 5)

        if num_total == i:
            sum_total += num_total

    return sum_total


def problem_31() -> int:
    coins = (1, 2, 5, 10, 20, 50, 100, 200)
    target = 200

    permutations = [()]  # List of tuples of already tried combinations.
    correct_permutations = [()]

    def create_perm() -> tuple:
        pass


def problem_45() -> int:

    tri = lambda n: n * (n + 1) / 2
    pent = lambda n: n * (3 * n - 1) / 2
    hex = lambda n: n * (2 * n - 1)

    tris = []
    pents = set()
    hexes = set()

    for i in range(2, 1000000):
        tris.append(tri(i))
        pents.add(pent(i))
        hexes.add(hex(i))

    list = []

    for tri in tris:
        if tri in pents and tri in hexes:
            list.append(tri)

    return list[1]


def problem_48():
    val = 0

    for i in range(1, 1000):
        val = val + i ** i

    str_val = str(val)

    return str_val[-10:]


def problem_52():
    for i in range(1, 200000):

        nums = set()

        num_as_str = str(2 * i)
        for c in num_as_str:
            nums.add(c)

        is_perm = True

        for j in range(3, 7):
            num_as_str = str(j * i)
            for c in num_as_str:
                if not nums.__contains__(c):
                    is_perm = False

        if is_perm:
            return i



def problem_55() -> int:

    numb = 1

    for i in range(197, 10000):

        j = i
        num_str = str(j)
        rev = num_str[::-1]
        num = int(rev)

        count = 1

        if Util.Util.is_pal(j):
            numb += 1

        elif count > 50:
            pass
    return 0


def main():
    print(problem_52())


main()
