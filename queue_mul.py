import Twitter2Video
import queue
import threading
import multiprocessing
import os

q = queue.Queue()
threads = []
def Mul_Threads(item_list,num):
  if item_list == []:
    return "No twitter names entered"
  if num == 0:
    return "The num should be bigger than 0"
  #nn = num.copy()
  def Thread():
    while True:
      #if q.empty():
        #break
      item = q.get()
      if item is None: break
      print("Thread {} is processing".format(item))
      Twitter2Video.tweet2image(item)
      Twitter2Video.image2video(item)
      print("Thread {} has completed".format(item))
      q.task_done()
      #if q.empty():
        #break


  for i in range(num):
    t = threading.Thread(target = Thread)
    t.start()
    threads.append(t)
  for item in item_list:
    q.put(item)
  q.join()
  for i in range(num):
    q.put(None)
  for t in threads:
    t.join()
  print()
  print("All threads have completed")
  return "All threads have completed!"

#item_list = ['BU_Tweets','CNN','Nike','mfaboston']
#item_list_2 = ['BU_Tweets', 'CNN', 'Nike', 'mfaboston', 'BU_ece', 'BostonDynamics', 'realDonaldTrump', 'WHO', 'TIME']
#Mul_Threads(item_list,4)
#Mul_Threads(item_list_2,6)
'''
print(os.path.exists('BU_Tweets.avi') == True)
print(os.path.exists('CNN.avi') == True)
print(os.path.exists('Nike.avi') == True)
print(os.path.exists('mfaboston.avi') == True)
print(os.path.exists('tttttt.avi') == True)
'''