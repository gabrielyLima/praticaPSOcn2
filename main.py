from fitness import rastrigin
from fitness import rosenbrock
from fitness import sphere
from pso import PSO

def main():

    error_all = []
    max_iterations = 10000
    executions = 30
    for _ in range(executions):
        p = PSO(sphere, [(-5.12, 5.12) for _ in range(30)], 30, max_iterations, 0.8, "LOCAL")
        print(p.best_position)
        print(p.best_error)
        error_all.append(p.error_history)
        print(p.error_history)
        arquivo2 = open('melhoresErrosSphereLocalClerc.txt', "a")
        arquivo2.writelines(str(p.best_error) + ", ")

    avg_error = []
    for i in range(max_iterations):
        sum = 0
        for j in range(executions):
            sum += error_all[j][i]
        media = sum/executions
        avg_error.append(media)

    print(avg_error)

    for y in range(len(avg_error)):
        arquivo = open('sphereLocalClerc.txt', "a")
        arquivo.writelines(str(avg_error[y]) + ", ")

if __name__ == "__main__":
    main()