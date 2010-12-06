# -*- coding: utf-8 -*-

import numpy
import string
import sys

class Conv:
	
	cont = None

	def convert(self,q0,x,y,q1,z,alf,t,fim):	
	  
		
		for f in fim:
			t.append([f,'$','$','p','→'])
			t.append(['p','e','e','Y','↓'])
			for a in alf:
				t.append(['p',a,a,'N','↓'])
		
		t0='t'+str(self.cont)
		t1='t'+str(self.cont+1)
		t2='t'+str(self.cont+2)
	  
		if(y=='e' and z=='e'):		
			t.append([q0,x,x,q1,'→'])
		 
		elif(y=='e' and z!='e'):
			t.append([q0,x,'T',t0,'→'])
			for a in alf:
				t.append([t0,a,a,t0,'→'])	
			t.append([t0,'e',z,t1,'←'])
			for a in alf:
				t.append([t1,a,a,t1,'←'])
			t.append([t1,'T',x,q1,'→'])
			self.cont=self.cont+2
			
		elif(y!='e' and z=='e'):
			t.append([q0,x,'T',t0,'→'])
			for a in alf:
				t.append([t0,a,a,t0,'→'])
			t.append([t0,'e','e',t1,'←'])
			t.append([t1,y,'e',t2,'←'])
			for a in alf:
				t.append([t2,a,a,t2,'←'])
			t.append([t2,'T',x,q1,'→'])
			self.cont= self.cont+3
			
		elif(y!='e' and z!='e'):
			t.append([q0,x,'T',t0,'→'])
			for a in alf:
				t.append([t0,a,a,t0,'→'])
			t.append([t0,'e','e',t1,'←'])
			t.append([t1,y,z,t2,'←'])
			for a in alf:
				t.append([t2,a,a,t2,'←'])
			t.append([t2,'T',x,q1,'→'])
			self.cont=self.cont+3
			
	def __init__(self):
		
		self.cont = 0
	
def concatena (word):
	
	newword = ''
	for i in word:
		if (i=='e'):
			newword = newword + ''
		else:
			newword = newword + i
	return newword

def removebarran(input):
	output=[]
	for line in input:
		line=line.strip('\n')
		output.append(line)
	return output

def main(args):
	input = file(args[0]).readlines()
	input=removebarran(input)
	num_state = int(input[0])
	alf = input[1].split('\t')
	#alf.remove('\n')
	state_ini = input[3].split('\t')
	#state_ini.remove('\n')
	state_fim = input[4].split('\t')
	#state_fim.remove('\n')
	trans = []


	for i,j in enumerate(input):
		if (i >= 5):
			aux = j.split('\t')
			#aux.remove('\n')
			trans.append(aux)

	newtrans = [['s','e','e',state_ini[0],'→']]
	lista = []
	opcao = 0
	passo = 1
	while (opcao != 2):
		print 'Gostaria de informar a palavra? '
		print '1. Sim'
		print '2. Nao'
		print 'Opcao: '
		opcao = int(raw_input())	
		if (opcao == 1):
		
			print ''
			print 'Informe a palavra:'
			word = list(raw_input())
			word.insert(0,'e')
			word.append('$')
			alf.append('$')
			estado = 0
			cursor = 0
			pos = 0
			Y = 0
			c = Conv()

			for t in trans:	
				c.convert(t[0],t[1],t[2],t[3],t[4],alf,newtrans,state_fim)
	
			estado = 's'
			cursor = word[pos]
		
		
			print ''
			print 'Computacao'
			print	'----------------------------------------------------------------------------------------------------'
			print	'     ','		','Est.','		','    ','		','Simb.','		','Simb.','		','   ','		','Est.'
			print	'Passo','		','Act.','		','Fita','		','Lido ','		','Escr.','		','Mv.','		','Novo'
			print	'-----','		','------','		','----','		','-----','		','-----','		','---','		','----'

			while estado!='N' and estado!='Y': 
	
				N = 1
				cont = 0
	
				while (cont < len(newtrans)):
					i = newtrans[cont]
				
				
					if (estado == i[0] and cursor == i[1]):		
						newword = concatena(word)
						#print '(',estado,',',i[4],newword,' cursor = ',cursor,'posiçao = ',pos,')'										
						print	passo,'		',estado,'		',newword,'		',cursor,'		',i[2],'		',i[4],'		',i[3]
						passo = passo + 1
						estado = i[3]
						word[pos] = i[2]		
						if (i[4] == '→'):
							pos = pos + 1			
						elif (i[4] == '←'):
							pos = pos - 1
						try:
							cursor = word[pos]
						except:
							word.append('e')
							cursor='e'
						N=0
						if (estado == 'Y' or estado == 'N'):						
							print	passo,'		',estado,'		',newword,'		',cursor,'		',i[2],'		',i[4],'		',i[3]						
							passo = passo + 1
						cont = len(newtrans)+1
					cont = cont + 1
	 
				if(N==1):
					estado = 'N'    
  
			if(estado=="Y"):
			
				print	'----------------------------------------------------------------------------------------------------'
				print ''
				print "palavra aceita"
				print ''
	
			elif(estado=="N"):
	
				print	'----------------------------------------------------------------------------------------------------'
				print ''
				print "palavra rejeitada"
				print ''
	
			else:
			
				print	'----------------------------------------------------------------------------------------------------'
				print ''
				print "erro"

		elif (opcao == 2):
		
			print 'Saindo do programa...'
		
if __name__ == "__main__":
    main(sys.argv[1:])
