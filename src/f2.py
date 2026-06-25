import cv2
import numpy as np
def showall(l):
    v=1
    for i in l:
        cv2.imshow("window"+str(v),i)
        v+=1
    cv2.waitKey(0)
def rectfind(contours):
    rect=[]
    for i in contours:
        area=cv2.contourArea(i)
        if area >40:
            peri =cv2.arcLength(i,True)
            app=cv2.approxPolyDP(i,0.02*peri,True)
           # print ("area",area,"points",app)
            if len(app)==4:
                rect.append(i)
    rect=sorted(rect,key=cv2.contourArea,reverse=True)
    return rect
def findcorner(contours):
    peri = cv2.arcLength(contours, True)
    app = cv2.approxPolyDP(contours, 0.02 * peri, True)
    return app
def imgsplit(parts,omr_type):
    if omr_type==1:
        no_of_qs=45
        limitingvalue=1700
    elif omr_type==2:
        no_of_qs=90
        limitingvalue = 2700

    elif omr_type==3:
        no_of_qs=180
        limitingvalue = 2700

    elif omr_type==4:
        no_of_qs=30
        limitingvalue = 1700

    qno=[]
    bubbles=[]
    d={}
    q=1
    t=0
    qs = np.vsplit(parts, no_of_qs)

    for r in qs:
        ans=[]
        m_value=[]
        qno.append(r)
        bubble=np.hsplit(r,4)
        n=1
        for b in bubble:
            t+=1
            m=cv2.countNonZero(b)
            bubbles.append(b)
            #print("bubbleno",t)
            print(q,m)
            if m>=limitingvalue:
                ans.append(n)
                m_value.append(m)
            n+=1
        try:
            max_ = max(m_value)
            i = m_value.index(max_)
            for z in ans:
                if ans.index(z) == i:
                    ans = [z]
        except:
            pass
        d[q]=ans
        q+=1
    return [qno,bubbles,d]
def corrector(dans,dmarked,cm=4,wm=1):
    for k in dans:
        v=dans[k]
        if v =="N":
            dans[k]=0
        elif v=="A":
            dans[k]=1
        elif v=="B":
            dans[k]=2
        elif v=="C":
            dans[k]=3
        elif v=="D":
            dans[k]=4

    l=len(dans)+1
    c=0
    w=0
    u=0
    cans=[]
    wans=[]
    unans=[]
    print(dans)
    for i in range(1,l):
        if len(dmarked[i])==1:

            if   dans[i]==dmarked[i][0]:
                c+=1
                cans.append(i)
            else:
                w+=1
                wans.append(i)
        elif len(dmarked[i])!=1 or dans[i] ==0:
            u+=1
            unans.append(i)
    marks=c*cm-w*wm
    print(cans,unans,wans)
    d={"CORRECT QUESTIONS":cans,"WRONG QUESTIONS":wans,"UNATTEMPTED QUESTIONS":unans,"MARKS":marks}


    return d













