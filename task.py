qa=int(input("Quantity of product A: "))
wa=int(input("Do you want product A wrapped as a gift? Yes=1 or No=2: "))
qb=int(input("Quantity of product B: "))
wb=int(input("Do you want product B wrapped as a gift? Yes=1 or No=2: "))
qc=int(input("Quantity of product C: "))
wc=int(input("Do you want product C wrapped as a gift? Yes=1 or No=2: "))


def offerFunction(qa,qb,qc,wa,wb,wc):
    tq=qa+qb+qc
    tpa=qa*20
    tpa1=tpa
    tpb=qb*40
    tpb1=tpb
    tpc=qc*50
    tpc1=tpc
    tp=tpa+tpb+tpc
    tp1=tp
    op1=op2=op3=op4=tp
    offer=0
    if tp>200 or (qa>10 or qb>10 or qc>10) or tq>20 or tq>30:
        offer=1
        i=1
        while i<5:
            if i==1:
                if tp>200:
                    tp-=10
                    op1=tp
                    tp=tp1
                i+=1
            if i==2:
                if qa>10 or qb>10 or qc>10:
                    if qa>10:
                        tpa-=tpa*(5/100)
                    elif qb>10:
                        tpb-=tpb*(5/100)
                    elif qc>10:
                        tpc-=tpc*(5/100)
                    op2=tpa+tpb+tpc
                    tpa=tpa1
                    tpb=tpb1
                    tpc=tpc1
                i+=1
            if i==3:
                if tq>20:
                    tp-=tp*(10/100)
                    op3=tp
                    tp=tp1
                i+=1
            if i==4:
                if tq>30:
                    if (qa>15 and qb<=15 and qc<=15) or (qa<=15 and qb>15 and qc<=15) or (qa<=15 and qb<=15 and qc>15):
                        if qa>15:
                            n=qa-15
                            tpa=300+(n*10)
                            op4=tpa+tpb+tpc
                            tpa=tpa1
                        elif qb>15:
                            n=qb-15
                            tpb=600+(n*20)
                            op4=tpa+tpb+tpc
                            tpb=tpb1
                        elif qc>15:
                            n=qc-15
                            tpc=750+(n*25)
                            op4=tpa+tpb+tpc
                            tpc=tpc1
                i+=1
    list1=[op1, op2, op3, op4]
    op=min(list1)
    wpa=wpb=wpc=0
    if wa==1:
        wpa=qa
    if wb==1:
        wpb=qb
    if wc==1:
        wpc=qc
    gwp=wpa+wpb+wpc    
    np=tq/10
    x=type(np)
    if x!=int:
        np=tq//10+1    
    sp=np*5
    print("Product A Quantity: "+str(qa)+"  Total amount for product A: "+str(tpa))
    print("Product B Quantity: "+str(qb)+"  Total amount for product B: "+str(tpb))
    print("Product C Quantity: "+str(qc)+"  Total amount for product C: "+str(tpc))
    print("sub total: "+str(tp))
    if offer==1:
        if op==op1:
            print("offer: flat_10_discount \ndiscount amount: "+str(tp-op1))
        elif op==op2:
            print("offer: bulk_5_discount \ndiscount amount: "+str(tp-op2))
        elif op==op3:
            print("offer: bulk_10_discount \ndiscount amount: "+str(tp-op3))
        elif op==op4:
            print("offer: tiered_50_discount \ndiscount amount: "+str(tp-op4))
    else:
        print("offer: no offer applicable \ndiscount amount: "+str(0))
    print("shipping fee: "+str(sp)+" \ngift wrap fee: "+str(gwp))
    print("total: "+str(op+sp+gwp))



offerFunction(qa,qb,qc,wa,wb,wc)
