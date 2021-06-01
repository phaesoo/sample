from multiprocessing import Process, Queue
import numpy as np

# child process 개수
child_count = 5

# child process에서 실행될 method
def child_func(q):
    """
    비즈니스 로직 수행
    """
    
    # child_func수행 완료 후 결과를 queue에 put
    q.put(np.random.rand(5))


# Queue 및 Process 생성
queue_list = list()
process_list = list()
for _ in range(child_count):
    q = Queue()
    p = Process(target=child_func, args=(q,))
    
    queue_list.append(q)
    process_list.append(p)

# 모든 process start 
for p in process_list:
    p.start()

# Queue에서 결과 받아옴
results = [q.get() for q in queue_list]

# 모든 process join
for p in process_list:
    p.join()

print (results)

