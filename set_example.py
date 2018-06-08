
file_path = '/Users/huwang/Documents/Case/JokerCase_DATA/python/movies/day01/kaifangX.txt'
open_file = open(file_path, 'r', encoding='gbk', errors = 'ignore')

save_file = '/Users/huwang/Documents/Case/JokerCase_DATA/python/movies/day01/emial.txt'
open_save_file = open(save_file,'a')



def save_to_list(): 
	save_list = []
	i = 0
	while i < 1000:
		try:
			email = open_file.readline().split(',')[-2]
			print(email)
			if (email not in save_list) and (email.find('com') != -1):
				save_list.append(email)
				i += 1
		except Exception as e:
			continue
	save_to_txt(save_list)

def save_to_txt(save_list):
	for email in save_list:
		print(email)
		open_save_file.write(email + '\n')

	open_save_file.close()



if __name__ == '__main__':
	save_to_list()