from urllib2 import ProxyHandler,build_opener,install_opener,Request,urlopen
from threading import Thread
from os import name,system
from sys import exit


class GET_PROXIES(Thread):
	def __init__(self,range0=int(),range1=int(),range2=int(),range3=int(),max_range=int(),max_timeout=int(),out_file=str(),win_or_unix=None):
		self.range0 = range0
		self.range1 = range1
		self.range2 = range2
		self.range3 = range3

		self.max_range = max_range

		self.out_file = out_file

		self.win_or_unix = win_or_unix#True for linux || False for windows

		pass



	def write(self,ll):
		xx = open(self.out_file,"a")
		xx.write(ll+'\n')
		xx.close()



	def runner(self):



		C_found = 0
		C_error = 0
		C_not_response = 0
		

		for i0 in range(self.range0,self.max_range):
			for i1 in range(self.range1,self.max_range):
				for i2 in range(self.range2,self.max_range):
					for i3 in range(self.range3,self.max_range):
						ip_check = '{}.{}.{}.{}'.format(i0,i1,i2,i3)
						try:
							proxy_handler = ProxyHandler({'http':ip_check+':'+str(8080)})
							opener = build_opener(proxy_handler)
							install_opener(opener)
							req = Request("http://www.google.com")
							try:
								sock=urlopen(req, timeout= 7)
								rs = sock.read(1000)
								if '<title>Google</title>' in rs:
									C_found+=1
									print('[{}]FOUND[{}]'.format(C_found,C_found))
									self.write(ip_check)
								else:
									C_error+=1
									print('[{}]ERROR[{}]'.format(C_error,C_error))
							except Exception:
								C_not_response+=1
								print('[{}]TIMEOUT[{}]'.format(C_not_response,C_not_response))

						except Exception:
							exit(1)



def clear():
    command = 'clear'
    if name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    system(command)



def main():
	try:
		min_bit = raw_input('Choose your ip where you want start\n\nsuch as 1.1.1.1\n\n\n')
		max_bit = raw_input('Choose the number of ip that you want finish\n\nthe max is 255\n\n\n')
		file_out = raw_input('Choose the name of file where you want have the output of results!\n\n\n')
 

 
		rang0 = int(min_bit.split('.')[0])
		rang1 = int(min_bit.split('.')[1])
		rang2 = int(min_bit.split('.')[2])
		rang3 = int(min_bit.split('.')[3])
	except Exception as i:
		print(i)
		print('\n\n\nSomething wrong\n\nTRY AGAIN!')
		exit(1)



	obj = GET_PROXIES(range0=rang0,range1=rang1,range2=rang2,range3=rang3,max_range=int(max_bit),out_file=file_out)
	obj.runner()






if __name__ == '__main__':
	main()






