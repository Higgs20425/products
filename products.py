import os 

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, int(price)])
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name == 'q': #quit
			break
		price = input('請輸入商品金額: ')
		products.append([name, int(price)])
	print(products)
	return products

# 顯示輸入的商品
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

# 檢查檔案
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):
		print('有找到檔案!!')
		products = read_file('products.csv')
	else:
		print('找不到檔案...')	

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()