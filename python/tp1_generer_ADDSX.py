import math
#variables
nbt=0#nombre d'espaces
result=0#somme des chiffres
x="'"#apostrophe pour l'affichage
#################### Generateur ADDS1 ###########################################################

def genereADDS1():
		of=open("ADDS1.py","w")
		print ("def ADDS1(a,b):",file=of)
		x="'"
		for i in range (0,10):
				for j in range (0,10):
					x="'" #apostrophe pour l'affichage
					#if(a=='' and b=='')
					print("    if (a==",x+str(i)+x,"and b==",x+str(j)+x,"):",file=of)
					somme=i+j # somme des chiffres
					#return('','')
					print ("        return( ",x+str(somme%10)+x,",",x+str(somme//10)+x,")",file=of)
		print("    raise ValueError('unknown digits in ADDS1')",file=of)
		of.flush

##################### Generateur ADDS2 ###########################################################	
def genereADDS2():
		on=open("ADDS2.py","w")
		print ("def ADDS2(a,b):",file=on)
		for i in range(0,10):
				x="'"#apostrophe pour l'affichage
				print("    if(a==",x+str(i)+x,"):",file=on)
				for j in range (0,10):
						print("        if(b==",x+str(j)+x,"):",file=on)
						somme=str(i+j)#somme des chiffres
						if len(somme)>1:
								print("           return(",x+somme[0]+x,",",x+somme[1]+x,")",file=on)
						else:
								print("           return(",x+somme+x,",",x+str(0)+x,")",file=on)
		print("    raise ValueError('unknown digits in ADDS2')",file=on)
		on.flush
######################ADDS1BASE#########################################################

def genereADDS1Var():
		
		ok=open("ADDS1VAR.py","w")
		chiffres=[10,11,12,13,14,15]
		sxmboles=['A','B','C','D','E','F']
		#base 2 jusqu'au base 10
		for i in range (2,11):
				x="'"
				t="def ADDS1B"##affichage
				t=t+str(i)
				s="(a,b):"
				t=t+s
				t.strip()
				print (t,file=ok)
				for j in range (0,i):
						for k in range (0,i):
								x="'"
								x="'"
								print("    if (a==",x+str(j)+x,"and b==",x+str(k)+x,"):",file=ok)
								c=k+j
								z=c%i##idem que genereADDS1
								e=c//i
								print ("        return( ",x+str(z)+x,",",x+str(e)+x,")",file=ok)
				print("    raise ValueError('unknown digits in ADDS1')",file=ok)
				print("                                               ",file=ok)
		#base 11 jusqu'au base 16
		for l in range (11,17):
				f="def ADDS1B"
				f=f+str(l)
				p="(a,b):" #affichage
				f=f+p
				f.strip() #supression des espaces
				print (f,file=ok)
				for m in range (0,l):
						for n in range (0,l): #idem que genereADDS1()
								   x="'"
								   if((n>=10)&(m<10)):#changements des chiffres en caracteres

										   print("    if(a==",x+str(m)+x,"and b==",x+sxmboles[n-10]+x,"):",file=ok)
								   elif((m>=10)&(n<10)):
										   print("    if(a==",x+sxmboles[m-10]+x,"and b==",x+str(n)+x,"):",file=ok)
								   elif((m>=10)&(n>=10)):
										   print("    if(a==",x+sxmboles[m-10]+x,"and b==",x+sxmboles[n-10]+x,"):",file=ok)


								   else:
										   print("    if (a==",x+str(m)+x,"and b==",x+str(n)+x,"):",file=ok)
								   somme=m+n
								   z=somme%l
								   e=somme//l


								   if((z>=10)&(e<10)):
										   print ("        return( ",x+sxmboles[z-10]+x,",",x+str(e)+x,")",file=ok)
								   elif((e>=10)&(z<10)):
										   print ("        return( ",x+sxmboles[z-10]+x,",",x+str(e)+x,")",file=ok)

								   elif((e>=10)&(z>=10)):
										   print("    if(a==",x+sxmboles[e-10]+x,"and b==",x+sxmboles[z-10]+x,"):",file=ok)
								   else:
										   print ("        return( ",x+str(z)+x,",",x+str(e)+x,")",file=ok)

				print("    raise ValueError('unknown digits in ADDS1')",file=ok)
				print("                                               ",file=ok)                                           

		ok.flush
#####################ADDS2BASE#########################################################
def genereADDS2Var():
		chiffres=[10,11,12,13,14,15]
		sxmboles=['A','B','C','D','E','F']
		os=open("ADDS2VAR.py","w")
		#base 2 jusqu'au base 10
		for i in range (2,11):
				t="def ADDS2B"
				t=t+str(i)   #affichage
				t.strip()
				print (t,"(a,b):",file=os)
				for j in range (0,i):
						x="'"
						x="'"
						print("    if(a==",x+str(j)+x,"):",file=os)
						for k in range (0,i):
								print("        if(b==",x+str(k)+x,"):",file=os)
								somme=k+j
								e=somme%i #idem que genereADDS2()
								z=somme//i
								print ("            return( ",x+str(e)+x,",",x+str(z)+x,")",file=os)

				print("    raise ValueError('unknown digits in ADDS2')",file=os)
				print("                                               ",file=os)
		#base 11 jusqu'au base 16
		for l in range (11,17):
				f="def ADDS2B"
				f=f+str(l) #affichage
				f.strip()
				print (f,"(a,b):",file=os)
				for m in range (0,l):
						x="'"
						if(m>=10):
								print("    if(a==",x+sxmboles[m-10]+y,"):",file=os)
						else:

								print("    if(a==",x+str(m)+y,"):",file=os)

						for n in range (0,l):
								if(n>=10):
										print("        if(b==",x+symboles[n-10]+y,"):",file=os)
								else:
										print("        if(b==",x+str(n)+y,"):",file=os)
								somme=m+n
								e=somme%l #idem que genereADDS2()
								z=somme//l
								if((e>=10)&(z<10)):
										print ("            return( ",x+symboles[e-10]+y,",",x+str(z)+y,")",file=os)
								elif ((z>=10)&(e<10)):
										print ("            return( ",x+str(e)+y,",",x+symboles[z-10]+y,")",file=os)


								elif ((e>=10)&(z>=10)):

										print ("            return( ",x+symboles[e-10]+y,",",x+symboles[z-10]+y,")",file=os)

								else:
										print ("            return( ",x+str(e)+y,",",x+str(z)+y,")",file=os)

				print("    raise ValueError('unknown digits in ADDS2')",file=os)
				print("                                               ",file=os)                                           
		os.flush
###################################ADDS3########################################################

#################################  GenerateB1  #################################################
def genb1(b):#fonction qui va generer la 1ere partie pour les valeurs 0,1,2,4
	x="'"
	global nbt #nombre d'espaces
	global result
	
	nbt+=1
	if(b!=0):
		
		p= open("ADDS3.py","a")
		for i in range(0,nbt):
			print("    ",end='',file=p) #ajout des espaces
		print("if(b<="+x+str(b)+x+"):",file=p)
		p.close()
		
		genb1(b//2)
		
		p= open("ADDS3.py","a") ##ajout des espaces 
		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("else:",file=p)
		nbt+=1
##############################Traitement des cas spéciaux########################################


		if(math.floor(b/2) == b/2 ):

			if(b==2):
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("if(b<="+x+str(b+1)+x+"):",file=p)
				nbt=nbt+1
				
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("return("+x+str((result+b+1)%10)+x+","+x+str((result+b+1)//10)+x+")",file=p)
				nbt=nbt-1
				
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("else:",file=p)
				nbt=nbt+1
				
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("return("+x+str((result+b+2)%10)+x+","+x+str((result+b+2)//10)+x+")",file=p)
				nbt=nbt-3
				
		else:### b==1
			for i in range(0,nbt):
				print("    ",end='',file=p)
			print("return("+x+str((result+b+1)%10)+x+","+x+str((result+b+1)//10)+x+")",file=p)
			nbt=nbt-2
		p.close()

	else:#b==0
		p= open("ADDS3.py","a")
		
		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("if(b<="+x+str(b)+x+"):",file=p)
		nbt+=1

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("return("+x+str((result+b)%10)+x+","+x+str((result+b)//10)+x+")",file=p)
		nbt-=1

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("else:",file=p)
		nbt+=1

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("return("+x+str((result+b+1)%10)+x+","+x+str((result+b+1)//10)+x+")",file=p)
		nbt-=2
		
		p.close()
		return 0
#################################  GenerateB2  ################################
def genb2(b):#fonction qui va generer la 2eme partie pour les valeurs 5,6,7,9
	x="'"
	global nbt
	global result 
	nbt+=1
	if(b!=0):

		b+=5
		p= open("ADDS3.py","a")
		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("if(b<="+x+str(b)+x+"):",file=p)
		b-=5

		p.close()
		
		genb2(b//2)
		
		p= open("ADDS3.py","a")

		if(b!=4):
			b+=5
			for i in range(0,nbt):
				print("    ",end='',file=p)
			print("else:",file=p)
			nbt+=1
			b-=5
#######Traitement des cas speciaux#################################################################
		if(math.floor(b/2) == b/2 ):#################
			if(b==2):
				b+=5
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("if(b<="+x+str(b+1)+x+"):",file=p)##
				nbt=nbt+1
				
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("return("+x+str((result+b+1)%10)+x+","+x+str((result+b+1)//10)+x+")",file=p)
				nbt=nbt-1

				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("else:",file=p)
				nbt=nbt+1
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("return("+x+str((result+b+2)%10)+x+","+x+str((result+b+2)//10)+x+")",file=p)
				b-=5                
				nbt=nbt-3
			if(b==4):
				nbt-=1
				
		else:### b==1
			b+=5
			for i in range(0,nbt):
				print("    ",end='',file=p)
			print("return("+x+str((result+b+1)%10)+x+","+x+str((result+b+1)//10)+x+")",file=p)
			b-=5
			nbt=nbt-2
 
		p.close()

	else:
		b+=5
		p= open("ADDS3.py","a")

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("if(b<="+x+str(b)+x+"):",file=p)
		nbt+=1

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("return("+x+str((result+b)%10)+x+","+x+str((result+b)//10)+x+")",file=p)
		nbt-=1

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("else:",file=p)
		nbt+=1

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("return("+x+str((result+b+1)%10)+x+","+x+str((result+b+1)//10)+x+")",file=p)
		b-=5
		nbt-=2
		
		p.close()
		return 0

#################################  GenerateA1  ################################
def gena1(a):
	x="'"
	global nbt
	global result
	result=a
	nbt+=1
	if(a!=0):

		p= open("ADDS3.py","a")
		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("if(a<="+x+str(a)+x+"):",file=p)
		p.close()

		gena1(a//2)

		p= open("ADDS3.py","a")
		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("else:",file=p)
		if(a==2):
			nbt+=1
		p.close()
#######Traitement des cas spéciaux#################################################################

		p= open("ADDS3.py","a")
		if(math.floor(a/2) == a/2 ):#################
			if(a==2):
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("if(a<="+x+str(a+1)+x+"):",file=p)##
				p.close()
				
				genb1(4)
				nbt-=1
				genb2(4)
				result+=1
				
				p= open("ADDS3.py","a")
				nbt-=1
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("else:",file=p)
				nbt=nbt+1
				p.close()

				genb1(4)
				nbt-=1
				genb2(4)

				p= open("ADDS3.py","a")
	
				nbt=nbt-1
				result+=1                
				nbt=nbt-3
			if(a==4):
				nbt-=1
		else:

			p.close()

			genb1(4)
			nbt-=1
			genb2(4)

			p= open("ADDS3.py","a")

			result+=1
			nbt=nbt-2

		p.close()
####### 
		
	else: 
		p= open("ADDS3.py","a")

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("if(a<="+x+str(a)+x+"):",file=p)
		p.close()


		genb1(4)
		nbt-=1
		genb2(4)
		result+=1

		p= open("ADDS3.py","a")
		
		nbt-=1

		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("else:",file=p)


		p.close()

		genb1(4)
		nbt-=1
		genb2(4)

	
		result+=1
		nbt-=2
		
		return 0

#################################  GenerateA2  ################################
	    #fonction qui va generer la 2eme partie pour les valeurs 5,6,7,9
def gena2(a):
	x="'"
	global nbt
	global result
	result=a+5
	nbt+=1
	if(a!=0):

		a+=5
		p= open("ADDS3.py","a")
		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("if(a<="+x+str(a)+x+"):",file=p)
		p.close()
		a-=5

		gena2(a//2)

		p= open("ADDS3.py","a")

		if(a!=4):
			for i in range(0,nbt):
				print("    ",end='',file=p)
			print("else:",file=p)
			if(a==2):
				nbt+=1
		p.close()
#######Traitement des cas spéciaux####################################################

		p= open("ADDS3.py","a")
		if(math.floor(a/2) == a/2 ):#################

			if(a==2):#a==2
				a+=5
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("if(a<="+x+str(a+1)+x+"):",file=p)
				p.close()

				genb1(4)
				nbt-=1
				genb2(4)
				result+=1

				p= open("ADDS3.py","a")
				nbt-=1
				for i in range(0,nbt):
					print("    ",end='',file=p)
				print("else:",file=p)
				nbt=nbt+1
				p.close()

				genb1(4)
				nbt-=1
				genb2(4)

				p= open("ADDS3.py","a")
				nbt=nbt-1
				result+=1
				a-=5
				result+=1
				nbt=nbt-3                
			if(a==4):
				nbt-=1
				

		else:### a==1
 
			p.close()
			genb1(4)
			nbt-=1
			genb2(4)
			p= open("ADDS3.py","a")
			result+=1
			nbt=nbt-2
		p.close()
####### 
		
	else: ## a==0
		a+=5
		p= open("ADDS3.py","a")
		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("if(a<="+x+str(a)+x+"):",file=p)

		p.close()
		genb1(4)
		nbt-=1
		genb2(4)
		result+=1
		
		p= open("ADDS3.py","a")        
		nbt-=1
		for i in range(0,nbt):
			print("    ",end='',file=p)
		print("else:",file=p)
		p.close()

		genb1(4)
		nbt-=1
		genb2(4)

	
		a-=5
		result+=1
		nbt-=2

		return 0

#################################  MAIN  ##################################       
def genereADDS3():
	global nbt
	p= open("ADDS3.py","w")
	print("def ADDS3(a,b):",file=p)
	p= open("ADDS3.py","a")
	gena1(4)
	nbt+=1
	gena2(4)
	print("    raise ValueError('unknown digits in ADDS3')",file=p)
