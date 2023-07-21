class LinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None
        
print("\n\t\t\t----------------------")
print("\t\t\tWELCOME TO FLAMES GAME\t\tBY : VYSAKH S")
print("\t\t\t----------------------\n")

#inputing two strings
a = input("ENTER 1ST PERSON NAME : ").lower()
b = input("ENTER 2ND PERSON NAME : ").lower()

x = a.split(" ")
a = list("".join(map(str,x)))
x = b.split(" ")
b = list("".join(map(str,x)))

if len(a)>len(b):
    a,b = b,a

#performing cancellation in two strings
c = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            a[i] = '*'
            b[j] = '*'
            c = c + 2
            break

#displaying the string after performing cancellation
print("\nFINAL STRINGS : "," ".join(map(str,a)),"\n\n\t\t"," ".join(map(str,b)),"\n")

# length of dissimilar string count
c = len(a)+len(b)-c
print("\nTHE COUNT IS : ",c)

# framing a circular doubly linked list of content F<=>L<=>A<=>M<=>E<=>S<=>F continues
flames = "FLAMES"
for i in flames:
    if i==flames[0]:
        head = LinkedList(i)
        cur1 = head
    else:
        cur2 = LinkedList(i)
        cur1.next = cur2
        cur2.prev = cur1
        cur1 = cur2
    if i==flames[-1]:
        cur2.next = head
        head.prev = cur2
        cur2 = head

# displaying circular doubly linked list of content F<=>L<=>A<=>M<=>E<=>S<=>F continues
print("\n------------")
current = head
while True and not None:
    print(current.val,end=" ")
    current = current.next
    if current == head:
        break
print("\n------------\n")
   
if c==0:
    # all same letters in strings
    print("YOU TWO BETTER DIE...WASTE OF WEIGHT FOR EARTH")
else:
    #have counts
    current = head
    t = 0
    while True:
        t = t + 1
        #count equals to c
        if t==c:
            
            print("REMOVED : ",current.val)
            current.prev.next = current.next
            rem = current.next
            current.next.prev = current.prev
            current = rem
            t = 1
           
            # final Outcome
            if current.next==current:
                r = current.val
                print("\nREMAINING IS : ",r,"\n")
                if r=='F':
                    print("CONGRATS YOU TWO ARE FRIENDS...")
                elif r=='L':
                    print("CONGRATS YOU TWO ARE LOVERS...")
                elif r=='A':
                    print("CONGRATS YOU TWO HAVE AFFECTION ON EACH...")
                elif r=='M':
                    print("CONGRATS YOU TWO WILL MARRY SOON...")
                elif r=='E':
                    print("CONGRATS YOU TWO ARE ENEMIES...")
                else:
                    print("CONGRATS YOU TWO ARE SIBLINGS...")
                   
                break
            
        # trversing the pointer
        current = current.next
        
print("\n\t\t\t------------------")
print("\t\t\tEND OF FLAMES GAME")
print("\t\t\t------------------\n")
