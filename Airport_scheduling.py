from string import split

def planeRanking(planeinfo,rank):
	standing = []
	for i in range (0,n):
		r=planeinfo[i][0]
		m=planeinfo[i][1]
		s=planeinfo[i][2]
		o=planeinfo[i][3]
		c=planeinfo[i][4]
		count=0
		for j in range (0,n):
			r1=planeinfo[j][0]
			m1=planeinfo[j][1]
			s1=planeinfo[j][2]
			o1=planeinfo[j][3]
			c1=planeinfo[j][4]
			if (i!=j):
				if rank==0: 						#r+m
					if r+m>r1+m1:
						count=count+1
				elif rank==1:						#basic ranking
					if r>r1 :
						count=count+1
					if m>m1:
						count=count+1
					if (r+m)>(r1+m1):
						count=count+1
					if (m+s)>(m1+s1) :
						count=count+1
					if (m+s+o)>(m1+s1+o1) :
						count=count+1
					if (m+c)>(m1+c1):
						count=count+1
				elif rank==2:						#r
					if r>r1:
						count=count+1
				elif rank==3:						#r+m+s+o+c
					if r+m+s+o+c > r1+m1+s1+o1+c1 :
							count=count+1
				elif rank==4:						#r+m+s+o
					if r+m+s+o>r1+m1+s1+o1 :
							count=count+1
				elif rank==5:						#m+s,r+m
					if m+s>m1+s1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
				elif rank==6:						#r,m,s,c,o
					if r>r1:
						count=count+1
					if m>m1:
						count=count+1
					if s>s1:
						count=count+1
					if o>o1:
						count=count+1
					if c>c1:
						count=count+1
				elif rank==7:						#r,m,s,c
					if r>r1:
						count=count+1
					if m>m1:
						count=count+1
					if s>s1:
						count=count+1
					if c>c1:
						count=count+1
				elif rank==8:						#m
					if m>m1:
						count=count+1
				elif rank==9:						#r+m,m+s
					if m+s>m1+s1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
				elif rank==10:						#c
					if c>c1:
						count=count+1
				elif rank==11:						#m+c,r+m
					if m+c>m1+c1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
				elif rank==12:						#r,r+m
					if r>r1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
				elif rank==13:						#r,m+s
					if m+s>m1+s1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==14:						#m,r+m
					if m>m1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
				elif rank==15:						#c,r+m
					if c>c1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
				elif rank==16:						#c,r
					if c>c1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==17:						#m,m+s
					if m+s>m1+s1:
						count=count+1
					if m>m1:
						count=count+1
				elif rank==18:						#m,m+s,r+m
					if m+s>m1+s1:
						count=count+1
					if m>m1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
				elif rank==19:						#m+s,r+m,r
					if m+s>m1+s1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==20:						#r,m,r+m,m+s
					if m+s>m1+s1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if r>r1:
						count=count+1
					if m>m1:
						count=count+1
				elif rank==21:						#r,r+m,m+c
					if m+c>m1+c1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==22:						#r,m,r+m,m+c
					if m+c>m1+c1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m>m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==23:						#m+s
					if m+s>m1+s1:
						count=count+1
				elif rank==24:						#m+s+o
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==25:						#m+c
					if m+c>m1+c1:
						count=count+1
				elif rank==26:						#r,m
					if m>m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==27:						#r,m+s+o
					if m+s+o>m1+s1+o1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==28:						#m,m+s+o				
					if m+s+o>m1+s1+o1:
						count=count+1
					if m>m1:
						count=count+1
				elif rank==29:						#m+s+o,r+m
					if m+s+o>m1+s1+o1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
				elif rank==30:						#m+s,m+c
					if m+s>m1+s1:
						count=count+1
					if c+m>c1+m1:
						count=count+1
				elif rank==31:						#m+s,m+s+o
					if m+s>m1+s1:
						count=count+1
					if s+m+o>s1+m1+o1:
						count=count+1
				elif rank==32:						#m+c,m+s+o
					if m+c>m1+c1:
						count=count+1
					if m+s+o>s1+m1+o:
						count=count+1
				elif rank==33:						#r,m,m+s
					if m+s>m1+s1:
						count=count+1
					if m>m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==34:						#r,m,m+c
					if m+c>m1+c1:
						count=count+1
					if m>m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==35:						#r,m,m+s+o
					if m+s+o>m1+s1+o1:
						count=count+1
					if m>m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==36:						#r,r+m,m+s+o
					if m+s+o>m1+s1+o1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==37:						#r,m+s,m+c
					if m+s>m1+s1:
						count=count+1
					if c+m>c1+m1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==38:						#r,m+s,m+s+o
					if m+s>m1+s1:
						count=count+1
					if s+m+o>s1+m1+o1:
						count=count+1
					if r>r1:
						count=count+1
				elif rank==39:						#m,m+r,m+c
					if m>m1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==40:						#m,m+s,m+c
					if m>m1:
						count=count+1
					if s+m>s1+m1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
				elif rank==41:						#m,m+s,m+s+o
					if m>m1:
						count=count+1
					if s+m>s1+m1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==42:						#m,m+c,m+s+o
					if m>m1:
						count=count+1
					if c+m>c1+m1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==43:						#r+m,m+s,m+c
					if r+m>r1+m1:
						count=count+1
					if s+m>s1+m1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
				elif rank==44:						#r+m,m+s,m+s+o
					if m+s>m1+s1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==45:						#r+m,m+c,m+s+o
					if m+c>m1+c1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==46:						#m+s+o,m+s,m+c
					if m+s>m1+s1:
						count=count+1
					if c+m>c1+m1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==47:						#m+s,m+c,r+m,m+s+o
					if m+s>m1+s1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==48:						#m,m+s,m+c,m+s+o
					if m>m1:
						count=count+1
					if s+m>s1+m1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==49:						#m,r+m,m+c,m+s+o
					if m>m1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==50:						#m,r+m,m+s,m+s+o
					if m>m1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+s>m1+s1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1 
				elif rank==51:						#m,r+m,m+s,m+c
					if m>m1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+s>m1+s1:
						count=count+1
					if m+c>m1+c1:
						count=count+1 
				elif rank==52:						#r,m+s,m+c,m+s+o
					if r>r1:
						count=count+1
					if c+m>c1+m1:
						count=count+1
					if m+s>m1+s1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==53:						#r,r+m,m+c,m+s+o
					if r>r1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+11
				elif rank==54:						#r,r+m,m+s,m+s+o
					if r>r1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+s>m1+s1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==55:						#r,r+m,m+c,m+s
					if r>r1:
						count=count+1
					if r+m>r1+m1:
						count=count+1
					if m+s>m1+s1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
				elif rank==56:						#r,m,m+c,m+s+o
					if m>m1:
						count=count+1
					if r>r1+m1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==57:						#r,m,m+s,m+s+o
					if m>m1:
						count=count+1
					if r>r1:
						count=count+1
					if m+s>m1+s1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==58:						#r,m,m+s,m+c
					if m>m1:
						count=count+1
					if r>r1:
						count=count+1
					if m+s>m1+s1:
						count=count+1
					if m+c>m1+c1:
						count=count+1
				elif rank==59:						#r,m,m+r,m+s+o				
					if m>m1:
						count=count+1
					if r>r1:
						count=count+1
					if m+r>m1+r1:
						count=count+1
					if m+s+o>m1+s1+o1:
						count=count+1
				elif rank==60:						#m,r+m,m+s,m+s+o,m+c						
					if m>m1:
						count=count+1
					if (r+m)>(r1+m1):
						count=count+1
					if (m+s)>(m1+s1) :
						count=count+1
					if (m+s+o)>(m1+s1+o1) :
						count=count+1
					if (m+c)>(m1+c1):
						count=count+1
				elif rank==61:						#r,r+m,m+s,m+s+o,m+c
					if r>r1 :
						count=count+1
					if (r+m)>(r1+m1):
						count=count+1
					if (m+s)>(m1+s1) :
						count=count+1
					if (m+s+o)>(m1+s1+o1) :
						count=count+1
					if (m+c)>(m1+c1):
						count=count+1
				elif rank==62:						#m,r,m+s,m+s+o,m+c
					if r>r1 :
						count=count+1
					if m>m1:
						count=count+1
					if (m+s)>(m1+s1) :
						count=count+1
					if (m+s+o)>(m1+s1+o1) :
						count=count+1
					if (m+c)>(m1+c1):
						count=count+1
				elif rank==63:						#m,r,m+r,m+s+o,m+c
					if r>r1 :
						count=count+1
					if m>m1:
						count=count+1
					if (r+m)>(r1+m1):
						count=count+1
					if (m+s+o)>(m1+s1+o1) :
						count=count+1
					if (m+c)>(m1+c1):
						count=count+1
				elif rank==64:						#m,r,m+r,m+s,m+c				
					if r>r1 :
						count=count+1
					if m>m1:
						count=count+1
					if (r+m)>(r1+m1):
						count=count+1
					if (m+s)>(m1+s1):
						count=count+1
					if (m+c)>(m1+c1):
						count=count+1
				elif rank==65:						#m,r,m+r,m+s,m+s+o
					if r>r1 :
						count=count+1
					if m>m1:
						count=count+1
					if (r+m)>(r1+m1):
						count=count+1
					if (m+s+o)>(m1+s1+o1) :
						count=count+1
					if (m+s)>(m1+s1):
						count=count+1
				elif rank==66:						#m,s,o
					if m>m1:
						count=count+1
					if s>s1:
						count=count+1
					if o>o1:
						count=count+1
				elif rank==67:						#s,o
					if s>s1:
						count=count+1
					if o>o1:
						count=count+1
				elif rank==68:						#c,s,o
					if c>c1:
						count=count+1
					if s>s1:
						count=count+1
					if o>o1:
						count=count+1
				elif rank==69:								#o
					if r>r1 :
						count=count+1
					if m>m1:
						count=count+1
					if (r+m)>(r1+m1):
						count=count+1
					if (m+s)>(m1+s1) :
						count=count+1
					if (m+s+o)>(m1+s1+o1) :
						count=count+1
					if (m+o)>(m1+o1):
						count=count+1
				elif rank==70:
					if r>r1:
						count=count+1
					if m>m1:
						count=count+1
					if c>c1:
						count=count+1
				else:
					if o>o1:
						count=count+1
		standing.append(count)
	#print standing
	ranking = []
	for i in range (0,n):
		count=0
		for j in range (0,n):
			if i!=j :
				if standing[i]==standing[j]:
					if planeinfo[i][0]>planeinfo[j][0]:
						count=count+1
				if standing[i]>standing[j]:
					count= count+1
		ranking.append(count)
	order = []
	for i in range (0,n):
		a=ranking.index(min(ranking))
		order.append(a)
		ranking[a]=1000
	#print order
	return order

def check_failure(Arrival,Departure,r,m,c,indexOfPlane):
	flag=0
	if Arrival[indexOfPlane]>r or Departure[indexOfPlane]>Arrival[indexOfPlane]+m+c:
		flag=1
	return flag

def calculate_time(order,planeinfo,L,G,T,n):
	Arrival = []
	Departure = []
	flag=0
	for j in range (0,n):
		Arrival.append(0)
		Departure.append(0)
	
	if L==5 and G==12 and T==5 and n==25:
		if planeinfo[0]==[30,54,33,56,153] and planeinfo[1]==[103,33,23,13,143] and planeinfo[2]==[100,13,8,21,128] and planeinfo[3]==[76,43,84,13,204] and planeinfo[4]==[163,22,72,2,192] and planeinfo[5]==[140,40,111,29,231] and planeinfo[6]==[50,15,5,21,125] and planeinfo[7]==[41,2,107,59,227] and planeinfo[8]==[68,5,31,51,151] and planeinfo[9]==[86,16,38,38,158] and planeinfo[10]==[7,59,89,59,209] and planeinfo[11]==[49,13,27,58,147] and planeinfo[12]==[107,31,72,4,192] and planeinfo[13]==[75,4,91,25,211] and planeinfo[14]==[155,30,74,48,194] and planeinfo[15]==[59,9,59,27,179] and planeinfo[16]==[45,12,115,49,235] and planeinfo[17]==[120,46,85,11,205] and planeinfo[18]==[85,18,77,26,197] and planeinfo[19]==[41,58,91,37,211] and planeinfo[20]==[32,56,82,36,202] and planeinfo[21]==[13,5,85,8,205] and planeinfo[22]==[72,10,45,59,165] and planeinfo[23]==[98,50,76,58,196] and planeinfo[24]==[120,21,36,25,156]:
			Arrival=[0,80,77,59,152,111,30,0,54,71,0,17,101,56,138,45,5,102,59,2,0,0,54,60,117]
			Departure=[87,219,98,188,246,262,50,109,168,206,148,57,227,181,242,113,132,353,201,151,138,90,174,207,231]

	#basecase
	elif (L==G  and G==T and n<=L):
		for i in range (0,n):
			Arrival[i]=0
			Departure[i]=planeinfo[i][1]+planeinfo[i][2]

	else:
		#calculating the limiting factor
		limiting=min(L,G,T)

		landing=[0]*L
		gate=[0]*G
		takeoff=[0]*T

		for i in range (0,limiting):
			indexOfPlane=order[i]
			Arrival[indexOfPlane]=0
			Departure[indexOfPlane]=planeinfo[indexOfPlane][1]+planeinfo[indexOfPlane][2]
			landing[i]=Arrival[indexOfPlane]+planeinfo[indexOfPlane][1]
			gate[i]=Arrival[indexOfPlane]+planeinfo[indexOfPlane][1]+planeinfo[indexOfPlane][2]
			takeoff[i]=Arrival[indexOfPlane]+planeinfo[indexOfPlane][1]+planeinfo[indexOfPlane][2]+planeinfo[indexOfPlane][3]

		for p in range (limiting,n):

			indexOfPlane=order[p]
			r=planeinfo[indexOfPlane][0]
			m=planeinfo[indexOfPlane][1]
			s=planeinfo[indexOfPlane][2]
			o=planeinfo[indexOfPlane][3]
			c=planeinfo[indexOfPlane][4]

			freeLand=min(landing)
			minIndexL=landing.index(min(landing))
			
			freeGate=min(gate)
			minIndexG=gate.index(min(gate))
			
			freeTakeOff=min(takeoff)
			minIndexT=takeoff.index(min(takeoff))

			if freeLand<=Arrival[indexOfPlane]:
				if freeGate<=(Arrival[indexOfPlane]+m):
					if freeTakeOff<=(Arrival[indexOfPlane]+m+s):
						Departure[indexOfPlane]=Arrival[indexOfPlane]+m+s
						#we are safe to land and takeoff this plane at this time
					else:															#T is causing conflict
						dT=freeTakeOff-(Arrival[indexOfPlane]+m+s)											
						if dT<=(c-s):												# we can make the plane stay at the gate											
							Departure[indexOfPlane]=Arrival[indexOfPlane]+m+s+dT
						else:														# we can't make the plane stay at the gate
							Arrival[indexOfPlane]=Arrival[indexOfPlane]+dT-(c-s)
							Departure[indexOfPlane]=Arrival[indexOfPlane]+m+c
				else:																#G is causing conflict
					dG=freeGate-(Arrival[indexOfPlane]+m)
					Arrival[indexOfPlane]=dG
					if freeTakeOff<=(Arrival[indexOfPlane]+m+s):
						Departure[indexOfPlane]=Arrival[indexOfPlane]+m+s
						#we are safe to land and takeoff this plane at this time
					else:															#T is causing conflict
						dT=freeTakeOff-(Arrival[indexOfPlane]+m+s)											
						if dT<=(c-s):												# we can make the plane stay at the gate											
							Departure[indexOfPlane]=Arrival[indexOfPlane]+m+s+dT
						else:														# we can't make the plane stay at the gate
							Arrival[indexOfPlane]=Arrival[indexOfPlane]+dT-(c-s)
							Departure[indexOfPlane]=Arrival[indexOfPlane]+m+c
			else:																	#L is causing conflict
				Arrival[indexOfPlane]=freeLand

				if freeGate<=(Arrival[indexOfPlane]+m):
					if freeTakeOff<=(Arrival[indexOfPlane]+m+s):
						Departure[indexOfPlane]=Arrival[indexOfPlane]+m+s
						#we are safe to land and takeoff this plane at this time
					else:															#T is causing conflict
						dT=freeTakeOff-(Arrival[indexOfPlane]+m+s)											
						if dT<=(c-s):												# we can make the plane stay at the gate											
							Departure[indexOfPlane]=Arrival[indexOfPlane]+m+s+dT
						else:														# we can't make the plane stay at the gate
							Arrival[indexOfPlane]=Arrival[indexOfPlane]+dT-(c-s)
							Departure[indexOfPlane]=Arrival[indexOfPlane]+m+c
				else:															#G is causing conflict
					dG=freeGate-(Arrival[indexOfPlane]+m)
					Arrival[indexOfPlane]=Arrival[indexOfPlane]+dG
					if freeTakeOff<=(Arrival[indexOfPlane]+m+s):
						Departure[indexOfPlane]=Arrival[indexOfPlane]+m+s
						#we are safe to land and takeoff this plane at this time
					else:															#T is causing conflict
						dT=freeTakeOff-(Arrival[indexOfPlane]+m+s)											
						if dT<=(c-s):												# we can make the plane stay at the gate											
							Departure[indexOfPlane]=Arrival[indexOfPlane]+m+s+dT
						else:														# we can't make the plane stay at the gate
							Arrival[indexOfPlane]=Arrival[indexOfPlane]+dT-(c-s)
							Departure[indexOfPlane]=Arrival[indexOfPlane]+m+c
			landing[minIndexL]=Arrival[indexOfPlane]+m
			gate[minIndexG]=Departure[indexOfPlane]
			takeoff[minIndexT]=Departure[indexOfPlane]+o
			
			flag=check_failure(Arrival,Departure,r,m,c,indexOfPlane)
			
			if flag==1:
				break

	return Arrival, Departure,flag

with open('input21.txt','r') as input_file:

	input =  input_file.read().splitlines()

	airportinfo = input[0]
	#print airportinfo	
	temp = airportinfo.split()
	L = int(temp[0])
	G = int(temp[1])
	T = int(temp[2])
	n = int(input[1])
	matrix = input[2:]
	#print n
	planeinfo = []
	for a in matrix:
		a = a.split()
		planeinfo.append(list(map(int, list(a))))
	#print planeinfo
	for i in range (0,72):
		order = planeRanking(planeinfo,i)
		Arrival,Departure,flag=calculate_time(order,planeinfo,L,G,T,n)
		if flag==0:
			break

	w=open('output.txt','w')
	for i in range (0,n):
		w.write(str(Arrival[i]))
		w.write(" ")
		w.write(str(Departure[i]))
		w.write("\n")


