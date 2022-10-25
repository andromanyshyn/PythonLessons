class MediaPlayer:

    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media1.play()

media2.open("filemedia2")
media2.play()


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        # for i in self.data:
        #     if self.LIMIT_Y[0] <= i <= self.LIMIT_Y[1]:
        #         print(i, end=" ")
        a, b = self.LIMIT_Y
        print(*filter(lambda x: a <= x <= b, self.data))


graph_1 = Graph()

graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()





