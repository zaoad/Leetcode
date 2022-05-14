
def threeSumMulti(arr: list, target: int) -> int:
        dict = {}
        for i in range(len(arr)):
            dict[arr[i]] = 1 if arr[i] not in dict else dict[arr[i]] + 1
        dict1=dict.copy()
        temp={}
        print(dict)
        mod = 1000000007
        ans = 0
        arr.sort()
        temp1={}
        for i in range(len(arr)):
            temp1[arr[i]] = 1 if arr[i] not in temp1 else temp1[arr[i]] + 1
            temp={}
            for j in range(i + 1, len(arr)):
                sum = arr[i] + arr[j];
                temp[arr[j]] = 1 if arr[j] not in temp else temp[arr[j]] + 1
                baki = target - sum
                print(i, j, arr[i], arr[j])
                print('baki', baki)
                if baki >= arr[j] and baki in dict:
                    minus = temp[baki] if baki in temp else 0
                    minus1 = temp1[baki] if baki in temp1 else 0
                    ans = ans + dict[baki]-minus-minus1;
                    print('ache', baki, dict[baki]);
                    print(temp, temp1)
                else:
                    print('nai')
                print('ans', ans)
        print(ans)

arr=[1,1,2,2,2,2]
target = 5
threeSumMulti(arr,target)

