# from maze.view.mazeapp import MazeApp
from maze.app.mazeapp import MazeApp, launch
from maze.generation.growingtree import GrowingTree
from maze.mazedata.board import Board, BoardSizeException


def main():
    try:
        test = Board(15, 15)
        generate = GrowingTree(test, 25)
        # generate.generate(10)
        run = MazeApp(test)
        run.maze_alg = generate
        run.on_execute()
        # while (not generate.complete()):
        #     s = input("step")
        #     generate.step()
        #     print(test)
        # print(test)
    except BoardSizeException as e:
        ex = e.message
        print(ex)


if __name__ == '__main__':
    launch()
    # main()
    # gt = GrowingTree(Board(), 50)
    # gt.generate(1)
    # ga = GeneticSolver(gt.board, 10000, 0.5, 10, 1)
    # sol = ga.simulate()
    # print(sol)
    # print(ga.fitness(sol))
    # print(ga.board)
