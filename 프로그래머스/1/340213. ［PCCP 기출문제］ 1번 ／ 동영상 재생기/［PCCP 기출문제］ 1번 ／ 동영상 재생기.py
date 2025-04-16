def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # prev는 10초 전 or 0 으로
    # next는 10초 후 or video_len
    # op_start ~ op_end 면 op_end로
    video_len_num = int(video_len[0]+video_len[1])*60 + int(video_len[3]+video_len[4])
    pos_num = int(pos[0]+pos[1])*60 + int(pos[3]+pos[4])
    op_start_num = int(op_start[0]+op_start[1])*60 + int(op_start[3]+op_start[4])
    op_end_num = int(op_end[0]+op_end[1])*60 + int(op_end[3]+op_end[4])
    
    for command in commands:
        if op_start_num <= pos_num <= op_end_num:
            pos_num = op_end_num
            
        if command == 'prev':
            pos_num -= 10
            if pos_num <= 0:
                pos_num = 0
        elif command == 'next':
            pos_num += 10
            if pos_num >= video_len_num:
                pos_num = video_len_num
        
        if op_start_num <= pos_num <= op_end_num:
            pos_num = op_end_num
    
    mm = str(pos_num // 60)
    ss = str(pos_num % 60)
    
    if len(mm) == 1:
        mm = "0"+mm
    if len(ss) == 1:
        ss = "0"+ss
        
    answer = mm + ":" + ss
    
    
    return answer