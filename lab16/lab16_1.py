import matplotlib.pyplot as plt
from collections import Counter


def main():
	def Open(name, mode):
		try:
			return open(name, mode, encoding="utf-8")
		except:
			print(f"There was an error while opening file {name}")
			return None

	def Read(file):
		file.seek(0)
		text = file.read().split()
		return text

	def count_words(text):
		words_count = 0
		for word in text:
			if not word.isdigit():
				words_count += 1
		return words_count

	def most_used_words(text):
		counter = Counter(text)
		most_used = counter.most_common(10)
		x = [most_used[el][0] for el in range(len(most_used))]

		y = [most_used[el][1] for el in range(len(most_used))]
		plt.bar(x, y)
		plt.title("10 найбільш вживаних слів у тексті")
		plt.xlabel("Слова")
		plt.ylabel("Зустрічаються разів у тексті")
		plt.tight_layout()
		plt.show()
		return most_used

	def extract_stopwords(text):
		# print(text)
		filename = "stopwords.txt"
		stopwords_file = open(filename, "r",
		                      encoding="utf-8")  # https://github.com/igorbrigadir/stopwords/blob/master/en/terrier.txt
		stopwords = [word.strip() for word in stopwords_file]
		print('Stopwords: ', stopwords)
		clean_text = [word.strip("\"'()“\n").rstrip("\",.'()“\n") for word in text if not word in stopwords]
		' '.join(clean_text)
		return clean_text

	mypath = "austen-sense.txt"
	file = Open(mypath, "r")
	counter = count_words(Read(file))
	print("Word counter:", counter)
	most_used = most_used_words(Read(file))
	print("Most used words:\n", most_used)

	clean_text = extract_stopwords(Read(file))

	most_used_cleaned = most_used_words(clean_text)
	print("Most used words in cleaned text without stopwords and punctuation:\n", most_used_cleaned)


if __name__ == '__main__':
	main()
