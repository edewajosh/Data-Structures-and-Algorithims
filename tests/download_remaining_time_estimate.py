import math

class RemainingTime:

    def __init__(self, file_size, file_size_downloaded, last_items):
        self.file_size = file_size
        self.file_size_downloaded = file_size_downloaded
        self.last_items = last_items

    def solution(self):
        if sum(self.file_size_downloaded) == self.file_size:
            return 0
        if len(self.file_size_downloaded) < self.last_items:
            average_of_last_items = sum(self.file_size_downloaded)/len(self.file_size_downloaded)
            return int(math.ceil(self.file_size/average_of_last_items))

        else:
            average_of_last_items = sum(self.file_size_downloaded[-self.last_items:])/self.last_items
            return int(math.ceil((self.file_size-sum(self.file_size_downloaded))/average_of_last_items))

if __name__ == '__main__':
    print("Downlaod time remaining estimate")
    obj = RemainingTime(100, [10,6,6,8], 2)

    print(obj.solution())