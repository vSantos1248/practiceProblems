n = int(input().strip())
contacts=[];
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op=="add": contacts.append(contact);
    else:
        count=0;
        for c in contacts:
            if contact==c[0:len(contact)]: count+=1;
        print(count);
