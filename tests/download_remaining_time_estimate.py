import math

class RemainingTime:

    def __init__(self, file_size, file_size_downloaded, last_items):
        self.file_size = file_size
        self.file_size_downloaded = file_size_downloaded
        self.last_items = last_items

    def solution(self):
        bytes_downloaded = sum(self.file_size_downloaded)
        number_downloaded = len(self.file_size_downloaded)
        if bytes_downloaded == self.file_size:
            return 0
        if number_downloaded < self.last_items:
            average_of_last_items = bytes_downloaded/number_downloaded
            return int(math.ceil((self.file_size-bytes_downloaded)/average_of_last_items))

        else:
            average_of_last_items = sum(self.file_size_downloaded[-self.last_items:])/self.last_items
            return int(math.ceil((self.file_size-bytes_downloaded)/average_of_last_items))

if __name__ == '__main__':
    print("Downlaod time remaining estimate")
    obj = RemainingTime(100, [10,10,10], 4)

    print(obj.solution())