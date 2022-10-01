import time
import sys

class do_remove:
	def __init__(self):
		self.wordList = []
		self.badList = []
		self.badList2 = []
		self.sorted_items = {}
		self.total_length_items = []
		self.dang = time.strftime('%H:%M:%S')
		self.open_file = input("[x] Your file : ")

	def remove(self):
		with open(open_file, 'r') as f:
			file = f.readlines()

		for line in file:
			line2 = line.split("|")
			if line2[0] in self.wordList:
				retrieved_elements = list(filter(lambda x: line2[0] in x, self.badList2))
				self.badList.append(line2[0])
				if retrieved_elements:
					pass
				else:
					self.badList2.append(line2[0])
			else:
				self.wordList.append(line2[0])
		start_time = time.time()	
		countd = 1
		print('[{0}]: {1} duplicate lines from {2}.'.format(self.dang, len(self.badList), "t.txt"))
		print("[{0}]: Total same item in shop : {1}" .format(self.dang,len(self.badList2)))
		print("[{}]: Processing to sort item" .format(self.dang))
		for same_items in self.badList2:
			for list_item_ in file:
				list_item__ = list_item_.split("|")
				if same_items in list_item__[0]:
					self.total_length_items.append(same_items)
			time.sleep(0.5)
			self.sorted_items[self.total_length_items[0]] = len(self.total_length_items)
			print("[{}][{}/{}]: Processing : {} | Found item {}" . format(self.dang,countd,len(self.badList2), same_items, len(self.total_length_items)), end='\r')
			self.total_length_items.clear()
			countd+=1

		print("")
		print("[{}][Checking Done] Result saved in result_sorted.txt" .format(self.dang))
		print("[x] Process Finished in {} Seconds" .format (time.time() - start_time))

if __name__ == "__main__":
	run=do_remove()
	run.remove()