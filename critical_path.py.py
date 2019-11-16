import colorama
from colorama import Fore, Back, Style
import plotly
import time, datetime
from tabulate import tabulate
import os,sys
import plotly.figure_factory as ff
colorama.init()

firstt = ' NETWORK ANALYSIS OF THE OPTIMAL SCHEDULING OF A LOCAL CAR PLANT ASSEMBLY'
lfirstt = len(firstt) + 5
spp = ''
for x in range(0,lfirstt):
    spp += ' '
dh = '\n'
print (Style.BRIGHT + Fore.RED + Back.WHITE + spp + dh + firstt + '     ' + dh + spp + Style.RESET_ALL)
print (Style.BRIGHT + Fore.YELLOW + dh +'Please kindly read the "How_to_use.txt" file to see how to use this program, thank you.......' + Style.RESET_ALL + dh)
def mainn():
    act = []
    pred = []
    dur = []
    start_act = []
    es = []
    temp_lis = []
    temp_lis2 = []
    db_pred = []
    fo_num = []
    norm_num = []
    opp_list = []
    opp_list2 = []
    opp_list3 = []
    doub_pred = []
    sing_pred = []
    dot_pred = []
    real_pred = []
    back_list = []
    bk_list = []
    db_checker = []
    new_lads = []
    total_float = []
    free_float = []
    critical_path = []
    big_start = []
    gantt_graph = []
    color = []
    lister = []
    lister2 = []
    slister = []
    slister2 = []
    numbe = str(input('\n' +'Enter the number of activities : '))
    term = 0
    if numbe == 'q':
        sys.exit()
    else:
        number = int(numbe)
    for y in range(number):
        x = str(input('Enter the activity, predecessor and duration : '))
        act.append(x.split(',')[0])
        pred.append(x.split(',')[1])
        dur.append(x.split(',')[2])

    for ob in pred:
        if '.' in ob:
            count1 = 0
            for dat in ob:
                if dat == '.':
                    count1 += 1
            for p in range(count1+1):
                temp_lis.append(ob.split('.')[p])
            db_pred.append(temp_lis)
            temp_lis = []

    for x in act:
        index = act.index(x)
        if pred[index] == 'n':
            y = 0 + int(dur[index])
            es.append(y)
        else:
            z = pred[index]
            if '.' in z:
                count2 = 0
                for dat in z:
                    if dat == '.':
                        count2 += 1
                for p in range(count2 + 1):
                    temp_lis2.append(z.split('.')[p])
                for char in temp_lis2:
                    f_index = act.index(char)
                    f_num = es[f_index]
                    norm_num.append(f_num)
                    r_num = int(f_num) + int(dur[index])
                    fo_num.append(r_num)
                
                max_num = max(fo_num)
                for char in temp_lis2:
                    f_index = act.index(char)
                    es[f_index] = int(max(norm_num))
                y = max_num
                es.append(y)
                temp_lis2 = []
                fo_num = []
                
            else:
                bindex = act.index(z)
                start = int(es[bindex])
                y = start + int(dur[index])
                es.append(y)

    len_act = len(act) + 1
    max_l = max(es)
    bk_list.append(max_l)
    for te in pred:
        if te == 'n':
            pass
        else:
            cou = pred.count(te)
            if cou > 1:
                if te in doub_pred:
                    pass
                else:
                    doub_pred.append(te)
            else:
                sing_pred.append(te)


    for x in pred:
        if x == 'n':
            pass
        else:
            if '.' in x:
                count5 = 0
                for p in x:
                    if p == '.':
                        count5 += 1
                for y in range(count5 + 1):
                    real_pred.append(x.split('.')[y])
            else:
                real_pred.append(x)

    for j in range(1,len_act):
        opp_list.append(act[-j])
        opp_list2.append(act[-j])


    for x in act:
        if x not in real_pred:
            ind7 = opp_list2.index(x)
            opp_list2.remove(x)
            opp_list2.insert(ind7,max_l)
            

    opp_list2[0] = max_l
    for k in range(1,len_act):
        opp_list3.append(pred[-k])

    for b in opp_list3:
        if b in doub_pred:
            if '.' in b:
                count0 = 0
                for x in b:
                    if x == '.':
                        count0 += 1
                for y in range(count0 + 1):
                    new_lads.append(b.split('.')[y])
                count1 = 0
                for cl in pred:
                    count1 += 1
                    if cl == b:
                        ind1 = count1-1
                        vali = act[ind1]
                        ind2 = opp_list.index(vali)
                        firs = opp_list2[ind2]
                        sec = int(dur[ind1])
                        res = firs - sec
                        db_checker.append(res)
                        min_no = min(db_checker)
                for d in new_lads:
                    ind3 = opp_list2.index(d)
                    opp_list2.remove(d)
                    opp_list2.insert(ind3, min_no)
                doub_pred.remove(b)
                db_checker = []
                new_lads = []
            else:
                count = 0
                for x in pred:
                    count += 1
                    if x == b:
                        ind1 = count-1
                        vali = act[ind1]
                        ind2 = opp_list.index(vali)
                        firs = opp_list2[ind2]
                        sec = int(dur[ind1])
                        res = firs - sec
                        db_checker.append(res)
                        min_no = min(db_checker)
                ind3 = opp_list2.index(b)
                opp_list2.remove(b)
                opp_list2.insert(ind3,min_no)
                doub_pred.remove(b)
                db_checker = []
        if b in sing_pred:
            if '.' in b:
                count0 = 0
                for x in b:
                    if x == '.':
                        count0 += 1
                for y in range(count0 + 1):
                    new_lads.append(b.split('.')[y])
                ind1 = pred.index(b)
                vali = act[ind1]
                ind2 = opp_list.index(vali)
                firs = opp_list2[ind2]
                sec = int(dur[ind1])
                res = firs - sec
                for x in new_lads:
                    dat = opp_list2.index(x)
                    opp_list2.remove(x)
                    opp_list2.insert(dat,res)
                new_lads = []
            else:
                ind1 = pred.index(b)
                vali = act[ind1]
                ind2 = opp_list.index(vali)
                firs = opp_list2[ind2]
                sec = int(dur[ind1])
                res = firs - sec
                ind3 = opp_list2.index(b)
                opp_list2.remove(b)
                opp_list2.insert(ind3,res)
            
    opp_list2.reverse()
    for al in act:
        y= act.index(al)
        x= pred[y]
        if x == 'n':
            sec = 0
            dura = int(dur[y])
            firs = int(opp_list2[y])
            firs2 = int(es[y])
            res = firs - sec - dura
            res2 = firs2 - sec - dura
            total_float.append(res)
            free_float.append(res2)
        elif '.' in x:
            for p in x:
                if p == '.':
                    pass
                else:
                    x = p
                    break
            z = act.index(x)
            sec = int(es[z])
            dura = int(dur[y])
            firs = opp_list2[y]
            firs2 = int(es[y])
            res =  firs - sec - dura
            res2 =  firs2 - sec - dura
            total_float.append(res)
            free_float.append(res2)
        else:
            z = act.index(x)
            sec = int(es[z])
            dura = int(dur[y])
            firs = opp_list2[y]
            firs2 = int(es[y])
            res =  firs - sec - dura
            res2 =  firs2 - sec - dura
            total_float.append(res)
            free_float.append(res2)



    count6 = -1
    for x in total_float:
        count6 += 1
        if x == 0:
            y = count6
            if free_float[y] == 0:
                term = act[y]
                critical_path.append(term)


    for items in act:
        i = act.index(items)
        if items in critical_path:
            resource = 'Critical activity'
            color.append('rgb(210, 60, 180)')
        else:
            resource = 'Non-critical activity'
            color.append('#7a0504')
        if pred[i] == 'n':
            dut = int(dur[i])
            du = str(dur[i])
            le = len(du)
            if le == 1:
                minsc = '0'+str(du)
                hrc = '00'
            else:
                if dut > 59:
                    
                    hr = str(int(dut/60))
                    mins = str(dut%60)
                    if len(hr) == 1:
                        hrc = '0'+str(hr)
                    else:
                        hrc = hr
                    if len(mins) == 1:
                        minsc = '0'+str(mins)
                    else:
                        minsc = mins
                else:
                    minsc = str(dut)
                    hrc = '00'
            starter = '2019-01-01 00:00:00'
            
                
            findex = int(es[i])
            finish = '2019-01-01 '+hrc+':'+minsc+':00'
            ress = dict(Task="Activity "+items, Start= starter, Finish=finish ,Resource = resource)
            gantt_graph.append(ress)
        else:
            kt = pred[i]
            if '.' in kt:
                kta = kt[0]
                ind9 = act.index(kta)
                dut = int(es[ind9])
                du = str(es[ind9])
                le = len(du)
                if le == 1:
                    minsc = '0'+str(dut)
                    hrc = '00'
                else:
                    if dut > 59:
                        hr = str(int(dut/60))
                        mins = str(dut%60)
                        if len(hr) == 1:
                            hrc = '0'+str(hr)
                        else:
                            hrc = hr
                        if len(mins) == 1:
                            minsc = '0'+str(mins)
                        else:
                            minsc = mins
                    else:
                        minsc = str(dut)
                        hrc = '00'
                dua = str(du)
                starter = '2019-01-01 '+hrc+':'+minsc+':00'
                findex = str((es[ind9]) + int(dur[i]))
                dut = int(findex)
                le = len(findex)
                if le == 1:
                    minsc = '0'+str(dut)
                    hrc = '00'
                else:
                    if dut > 59:
                        hr = str(int(dut/60))
                        mins = str(dut%60)
                        if len(hr) == 1:
                            hrc = '0'+str(hr)
                        else:
                            hrc = hr
                        if len(mins) == 1:
                            minsc = '0'+str(mins)
                        else:
                            minsc = mins
                    else:
                        minsc = str(dut)
                        hrc = '00'
                finish = '2019-01-01 '+hrc+':'+minsc+':00'
                ress = dict(Task="Activity "+items, Start= starter, Finish=finish, Resource = resource)
                gantt_graph.append(ress)
            else:
                
                ind9 = act.index(kt)
                du = str(es[ind9])
                dut = int(du)
                le = len(du)
                if le == 1:
                    minsc = '0'+str(dut)
                    hrc = '00'
                else:
                    if dut > 59:
                        hr = str(int(dut/60))
                        mins = str(dut%60)
                        if len(hr) == 1:
                            hrc = '0'+str(hr)
                        else:
                            hrc = hr
                        if len(mins) == 1:
                            minsc = '0'+str(mins)
                        else:
                            minsc = mins
                    else:
                        minsc = str(dut)
                        hrc = '00'
                starter = '2019-01-01 '+hrc+':'+minsc+':00'
                findex = str((es[ind9]) + int(dur[i]))
                dut = int(findex)
                le = len(findex)
                if le == 1:
                    minsc = '0'+str(dut)
                    hrc = '00'
                else:
                    if dut > 59:
                        hr = str(int(dut/60))
                        mins = str(dut%60)
                        if len(hr) == 1:
                            hrc = '0'+str(hr)
                        else:
                            hrc = hr
                        if len(mins) == 1:
                            minsc = '0'+str(mins)
                        else:
                            minsc = mins
                    else:
                        minsc = str(dut)
                        hrc = '00'
                finish = '2019-01-01 '+hrc+':'+minsc+':00'
                ress = dict(Task="Activity "+items, Start= starter, Finish=finish, Resource = resource )
                gantt_graph.append(ress)
    curr_date = datetime.datetime.now()
    data = ''
    sdata = ''
    opp_list.reverse()
    bc = '\033[1;36;40m'
    bw = '\033[1;37;40m'
    for items in act:
        activity = '\n\nACTIVITY '+ items + '\n'
        sactivity = Style.BRIGHT + Fore.CYAN +'\n\nACTIVITY '+ items + '\n'
        sitems = Style.BRIGHT + Fore.CYAN + 'Activity '+ str(items)
        ind = act.index(items)
        durati = dur[ind]
        preda = pred[ind]
        sdurati = Style.BRIGHT + Fore.GREEN + dur[ind]
        spreda = Style.BRIGHT + Fore.YELLOW + pred[ind]
        if items in critical_path:
            status =  'Critical'
            sstatus = Style.BRIGHT + Fore.YELLOW + 'Critical'
        else:
            sstatus = Style.BRIGHT + Fore.BLUE + 'Non-Critical'
            status = 'Non-Critical'
        sdata += sactivity
        data += activity
        ind10 = act.index(items)
        d_ind = int(dur[ind10])
        r_ind = pred[ind10]
        tff = int(total_float[ind10])
        stff = Style.BRIGHT + Fore.RED + str(total_float[ind10])
        fff =int(free_float[ind10])
        sfff = Style.BRIGHT + Fore.BLUE + str(free_float[ind10])
        if r_ind == 'n':
            estart = 0
            sestart = Style.BRIGHT + Fore.WHITE + str(estart) 
            data += 'Earliest start '+str(+estart) + ' min(s)' + '\n'
            sdata += Style.BRIGHT + Fore.WHITE + 'Earliest start '+str(sestart) + ' min(s)' + '\n'
            efinish = estart + (d_ind)
            sefinish = Style.BRIGHT + Fore.GREEN + str(efinish)
            data += 'Earliest finish = '+str(efinish) + ' min(s)' + '\n'
            sdata += Style.BRIGHT + Fore.WHITE + 'Earliest finish = '+str(sefinish) + ' min(s)' + '\n'
            lfinish = opp_list2[ind10]
            slfinish =  Style.BRIGHT + Fore.WHITE + str(lfinish)
            lstart = lfinish - d_ind
            slstart = Style.BRIGHT + Fore.WHITE + str(lstart)
            data += 'Latest start = '+str(lstart) + ' min(s)' + '\n'
            data += 'Latest finish = '+str(lfinish) + ' min(s)' + '\n'
            sdata += Style.BRIGHT + Fore.WHITE +'Latest start = '+str(slstart) + ' min(s)' + '\n'
            sdata += Style.BRIGHT + Fore.WHITE + 'Latest finish = '+str(slfinish) + ' min(s)' + '\n'
            data += 'Total float = '+str(tff) + ' min(s)' + '\n'
            sdata +=  Style.BRIGHT + Fore.WHITE +'Total float = '+str(stff) + ' min(s)' + '\n'
            data += 'Free float = '+str(fff) + ' min(s)' + '\n'
            sdata += Style.BRIGHT + Fore.WHITE + 'Free float = '+str(sfff) + ' min(s)' + '\n'
            data += 'Status = '+str(status) + '\n'
            sdata +=  Style.BRIGHT + Fore.WHITE + 'Status = '+str(sstatus) + '\n'
            lister = [activity,preda,durati,estart,efinish,lstart,lfinish,status,tff,fff]
            slister = [sitems,spreda,sdurati,sestart,sefinish,slstart,slfinish,sstatus,stff,sfff]
            lister2.append(lister)
            slister2.append(slister)
        else:
            if '.' in r_ind:
                rr_ind = r_ind[0]
                f_ind = opp_list.index(rr_ind)
                estart = int(es[f_ind])
                sestart = Style.BRIGHT + Fore.WHITE + str(estart) 
                data += 'Earliest start = '+str(+estart) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE + 'Earliest start '+str(sestart) + ' min(s)' + '\n'
                efinish = estart + d_ind
                sefinish = Style.BRIGHT + Fore.GREEN + str(efinish)
                data += 'Earliest finish = '+str(efinish) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE + 'Earliest finish = '+str(sefinish) + ' min(s)' + '\n'
                l_ind = opp_list.index(items)
                lfinish = int(opp_list2[l_ind])
                slfinish =  Style.BRIGHT + Fore.WHITE + str(lfinish)
                lstart = lfinish - d_ind
                slstart = Style.BRIGHT + Fore.WHITE + str(lstart)
                data += 'Latest start = '+str(lstart) + ' min(s)' + '\n'
                data += 'Latest finish = '+str(lfinish) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE +'Latest start = '+str(slstart) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE + 'Latest finish = '+str(slfinish) + ' min(s)' + '\n'
                data += 'Total float = '+str(tff) + ' min(s)' + '\n'
                sdata +=  Style.BRIGHT + Fore.WHITE +'Total float = '+str(stff) + ' min(s)' + '\n'
                data += 'Free float = '+str(fff) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE + 'Free float = '+str(sfff) + ' min(s)' + '\n'
                data += 'Status = '+str(status) + '\n'
                sdata +=  Style.BRIGHT + Fore.WHITE + 'Status = '+str(sstatus) + '\n'
                lister = [activity,preda,durati,estart,efinish,lstart,lfinish,status,tff,fff]
                slister = [sitems,spreda,sdurati,sestart,sefinish,slstart,slfinish,sstatus,stff,sfff]
                lister2.append(lister)
                slister2.append(slister)

            
            else:
                f_ind = opp_list.index(r_ind)
                estart = int(es[f_ind])
                sestart = Style.BRIGHT + Fore.WHITE + str(estart) 
                data += 'Earliest start = '+str(+estart) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE + 'Earliest start '+str(sestart) + ' min(s)' + '\n'
                efinish = estart + d_ind
                sefinish = Style.BRIGHT + Fore.GREEN + str(efinish)
                data += 'Earliest finish = '+str(efinish) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE + 'Earliest finish = '+str(sefinish) + ' min(s)' + '\n'
                l_ind = opp_list.index(items)
                lfinish = int(opp_list2[l_ind])
                slfinish =  Style.BRIGHT + Fore.WHITE + str(lfinish)
                lstart = lfinish - d_ind
                slstart = Style.BRIGHT + Fore.WHITE + str(lstart)
                data += 'Latest start = '+str(lstart) + ' min(s)' + '\n'
                data += 'Latest finish = '+str(lfinish) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE +'Latest start = '+str(slstart) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE + 'Latest finish = '+str(slfinish) + ' min(s)' + '\n'
                data += 'Total float = '+str(tff) + ' min(s)' + '\n'
                sdata +=  Style.BRIGHT + Fore.WHITE +'Total float = '+str(stff) + ' min(s)' + '\n'
                data += 'Free float = '+str(fff) + ' min(s)' + '\n'
                sdata += Style.BRIGHT + Fore.WHITE + 'Free float = '+str(sfff) + ' min(s)' + '\n'
                data += 'Status = '+str(status) + '\n'
                sdata +=  Style.BRIGHT + Fore.WHITE + 'Status = '+str(sstatus) + '\n'
                lister = [activity,preda,durati,estart,efinish,lstart,lfinish,status,tff,fff]
                slister = [sitems,spreda,sdurati,sestart,sefinish,slstart,slfinish,sstatus,stff,sfff]
                lister2.append(lister)
                slister2.append(slister)
    headerss = ['Activities','PD','DT','ES','EF','LS','LF','Status','TF','FF']
    itt = tabulate(slister2, headers = headerss)
    tt = tabulate(lister2, headers = headerss)
    witt = str(itt) + '\n'
    switt = str(tt) + '\n'
    firstt = ' NEW DATA CREATED ON '+ str(curr_date)
    lfirstt = len(firstt) + 5
    spp = ''
    for x in range(0,lfirstt):
        spp += ' '
    dh = '\n'
    timer = Style.BRIGHT + Fore.RED + Back.WHITE + dh+ spp+dh+firstt+'     '+dh+spp + Style.RESET_ALL + '\n'
    sp = Back.BLACK + '\n' + Style.RESET_ALL
    stimer =  '\n\nNEW DATA CREATED ON '\
            + str(curr_date) + '\n' + '\n'
    ssp = '\n'
    firstt = ' INDIVIDUAL ANALYSIS OF EACH ACTIVITY'
    lfirstt = len(firstt) + 5
    spp = ''
    for x in range(0,lfirstt):
        spp += ' '
    dh = '\n'
    total_data = timer + sp + witt + '\n' + Style.BRIGHT + Fore.RED + Back.WHITE +spp+dh+firstt+'     '+dh+spp  + Style.RESET_ALL + sdata
    print (total_data)
    stotal_data =  stimer + ssp + switt + '\n' + '\n\nINDIVIDUAL ANALYSIS OF EACH ACTIVITY \n' + \
                  data
    
    cp = ''

    duration = 0
    for x in critical_path:
        ind = act.index(x)
        val = dur[ind]
        duration += int(val)

    for x in critical_path:
        cp += str(x) + '   '
    stotal_data += '\nThe critical path is : ' + cp
    stotal_data += '\nThe Duration of activities in the critical path is : '+ str(duration) +' min(s)'
    curr_dir = os.getcwd()
    print (curr_dir)
    file_name = 'Data.txt'
    name = 'Data'
    name2 = 'Graph'
    if os.path.exists(name):
        os.chdir(name)
    else:
        os.mkdir(name)
        os.chdir(name)
    if os.path.isfile(file_name):
        rea = open(file_name, 'a+')
        rea.write(data)
        rea.close()
    else:
        rea = open(file_name, 'w+')
        rea.write(stotal_data)
        rea.close()

    os.chdir(curr_dir)

    if os.path.exists(name2):
        os.chdir(name2)
    else:
        os.mkdir(name2)
        os.chdir(name2)
    
     
    print (Style.BRIGHT + Fore.GREEN + 'The critical path is :' , Style.BRIGHT + Fore.RED + cp)
    print (Style.BRIGHT + Fore.GREEN + 'The Duration of activities in the critical path is :', duration,'min(s)')
    #print color
    #print gantt_graph
    print (Style.BRIGHT + Fore.YELLOW +"\n...Plotting the Gantt graph, please be patient.....\n")
    fig = ff.create_gantt(gantt_graph,colors = color, showgrid_x=True,index_col='Resource', showgrid_y=True,show_colorbar=True )
    plotly.offline.plot(fig, filename='Graph_Data.html')
    os.chdir(curr_dir)
    time.sleep(4)
    print (Style.BRIGHT + Fore.YELLOW +"...Graph has been plotted successfully.....")
    act = []
    pred = []
    dur = []
    start_act = []
    es = []
    temp_lis = []
    temp_lis2 = []
    db_pred = []
    fo_num = []
    norm_num = []
    opp_list = []
    opp_list2 = []
    opp_list3 = []
    doub_pred = []
    sing_pred = []
    dot_pred = []
    real_pred = []
    back_list = []
    bk_list = []
    db_checker = []
    new_lads = []
    total_float = []
    free_float = []
    critical_path = []
    big_start = []
    gantt_graph = []
    color = []
    lister = []
    lister2 = []
    slister = []
    slister2 = []
while True:
    try:
        mainn()
    except SystemExit:
        print (Style.BRIGHT + Fore.RED + '\nExiting now....')
        time.sleep(2)
        print (Style.BRIGHT + Fore.YELLOW + '\nThanks for using this program.....')
        time.sleep(2)
        sys.exit()
    except:
        print (Style.BRIGHT + Fore.RED + 'Sorry , an error occurred, Please make sure you READ the ' + Style.BRIGHT + Fore.YELLOW +'How_to_use.txt file to see how to use this program' + Style.BRIGHT + Fore.RED + ' or please enter the values correctly') 
    
