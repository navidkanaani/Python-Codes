count = int(input('Enter number of processes: '))  # count of processes
bt_list=[0 for i in range(count)] #burst list of processes

#get process details : burst time and quantum time, arrival time is same as process input index
def get_process_details(p_list):
    for i in range(count):
        print(f'\nEnter details for process [{i+1}]')
        print(f'Arrival Time: {i}') # this is constant
        p_list[i]=int(input('Burst Time: '))
    quantum=int(input('\nEnter Quantum Time: ')) #quantum time or time slice
    return turn_around_time_calc(bt_list,quantum) #calling turnaround time calculator

#calculate turnaround time
def turn_around_time_calc(bt_list,quantum):
    temp_bt=bt_list.copy() #a copy of burst times
    time=0 #current time
    tat_list=[0 for i in range(count)] #turnaround times list
    while(1): #because it must looping through the burst list until  the elements being 0
        done=True
        for t in range(count):
            if temp_bt[t]>0:
                if temp_bt[t]>=quantum:
                    temp_bt[t]-=quantum
                    time+=quantum
                    tat_list[t]+=time-tat_list[t]
                    done=False
                elif temp_bt[t]<quantum or temp_bt[t]==0:
                    time+=temp_bt[t]
                    temp_bt[t]=0
                    tat_list[t]+=time-tat_list[t]
                elif temp_bt[t]<0:
                    temp_bt[t]=0
        if done:
            break
    return waiting_time_calc(tat_list,bt_list) #calling waiting time calculator

#calculate waiting time for processes
def waiting_time_calc(tat_list,bt_list):
    wt_list=[0 for i in range(count)] #waiting times list
    for time in range(count):
        wt_list[time]=tat_list[time]-bt_list[time] #waiting time = turnaround time - burst time
    print(f'\nTurnaround times: {tat_list}') #printing turnaround times
    avg_calc('Turnaround Time',tat_list)  # calculating avg of turnaround times
    print(f'Waiting times: {wt_list}')
    avg_calc('Waiting Time',wt_list) #calculating avg of waiting times

#calculate avg
def avg_calc(type_list,list):
    s=0
    for i in list:
        s+=i
    avg=s/count
    return  print(f'Average {type_list} : {avg}') #return and print avg

#main
if __name__=='__main__':
    get_process_details(bt_list)

#This code contributed by Navid Kanaani