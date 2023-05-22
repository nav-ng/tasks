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
            elif i==2:
                if qa>10 or qb>10 or qc>10:
                    j=1
                    while j<4:
                        if j==1:
                            if qa>10:
                                tpa-=tpa*(0.05)
                            j+=1
                        elif j==2:
                            if qb>10:
                                tpb-=tpb*(0.05)
                            j+=1
                        elif j==3:        
                            if qc>10:
                                tpc-=tpc*(0.05)
                            j+=1    
                    op2=tpa+tpb+tpc
                    tpa=tpa1
                    tpb=tpb1
                    tpc=tpc1
                i+=1
            elif i==3:
                if tq>20:
                    tp-=tp*(0.1)
                    op3=tp
                    tp=tp1
                i+=1
            elif i==4:
                if tq>30:
                    if (qa>15 or qb>15 or qc>15):
                        k=1
                        while k<4:
                            if k==1: 
                                if qa>15:
                                    n=qa-15
                                    tpa=300+(n*10)
                                k+=1
                            elif k==2:
                                if qb>15:
                                    n=qb-15
                                    tpb=600+(n*20)
                                k+=1
                            elif k==3:
                                if qc>15:
                                    n=qc-15
                                    tpc=750+(n*25)
                                k+=1
                        op4=tpa+tpb+tpc
                        tpa=tpa1
                        tpb=tpb1
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
            print("offer applied: flat_10_discount \ndiscount amount: "+str(tp-op1))
        elif op==op2:
            print("offer applied: bulk_5_discount \ndiscount amount: "+str(tp-op2))
        elif op==op3:
            print("offer applied: bulk_10_discount \ndiscount amount: "+str(tp-op3))
        elif op==op4:
            print("offer applied: tiered_50_discount \ndiscount amount: "+str(tp-op4))
    else:
        print("no offer applicable for this purchase")
    print("shipping fee: "+str(sp)+" \ngift wrap fee: "+str(gwp))
    print("total amount to be paid: "+str(op+sp+gwp))



offerFunction(qa,qb,qc,wa,wb,wc)
