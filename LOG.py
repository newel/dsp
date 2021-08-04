#-*- coding:utf-8 -*-
import os
import csv
import struct

def readchar(fin):
    data = fin.read(1)
    outdata = struct.unpack('B', data)
    return int(outdata[0])

def readshort(fin):
    data = fin.read(2)
    outdata = struct.unpack('>H', data)
    return int(outdata[0])

def readint(fin):
    data = fin.read(4)
    outdata = struct.unpack('>I', data)
    return hex(outdata[0])

def read2_4bit(fin):
    rsltlist = []
    data = fin.read(1)
    outdata = struct.unpack('B', data)
    total = int(outdata[0])
    rsltlist.append((total>>4)&0xf)
    rsltlist.append(total&0xf)
    
    return rsltlist

def readDCIpayload(fin, ueidx, uenum):
    curpos = fin.tell()
    pos = uenum*12 - ueidx*12 + ueidx*8

    fin.seek(pos,1)
    dcipayload1 = readint(fin)
    dcipayload2 = readint(fin)
    fin.seek(curpos,0)
    return dcipayload1, dcipayload2
    
def readPuschCRC(fin):
    rsltlist = []
    data = fin.read(4)
    outdata = struct.unpack('>I', data)
    total = int(outdata[0])
    rsltlist.append((total>>31)&0x1)#tb_crc
    rsltlist.append(total&0x1ffffff)#cb_crc

    return rsltlist

def readPuschAck(fin):
    rsltlist = []
    data = fin.read(4)
    outdata = struct.unpack('>I', data)
    total = int(outdata[0])
    rsltlist.append((total>>20)&0x1)#ack_d
    rsltlist.append(total&0xfffff)#ack_val

    return rsltlist

def readPuschCSI(fin):
    rsltlist = []
    data = fin.read(4)
    outdata = struct.unpack('>I', data)
    total = int(outdata[0])
    rsltlist.append((total>>16)&0xffff)#cqi_amount
    rsltlist.append(total&0xffff)#ri_val

    return rsltlist

def readPuschOutAll(fin, ueidx, uenum):
    curpos = fin.tell()
    pos = uenum*120 - ueidx*120 + ueidx*20
    fin.seek(pos,1)
    
    uelist = []
    uelist.extend(readPuschCRC(fin))
    fin.seek(4, 1)
    uelist.extend(readPuschAck(fin))
    fin.seek(4, 1)
    uelist.extend(readPuschCSI(fin))
    
    fin.seek(curpos,0)

    return uelist

def readPucchOut(fin, ueidx, uenum):
    curpos = fin.tell()
    pos = uenum*32 - ueidx*32 + ueidx*16
    fin.seek(pos,1)
    
    uelist = []
    uelist.append(readchar(fin))
    uelist.append(readchar(fin))
    uelist.append(readchar(fin))
    uelist.append(readchar(fin))
    
    uelist.extend(read2_4bit(fin))
    uelist.extend(read2_4bit(fin))
    uelist.extend(read2_4bit(fin))
    uelist.extend(read2_4bit(fin))

    uelist.append(readchar(fin))
    uelist.append(readchar(fin))
    uelist.append(readshort(fin))
    uelist.append(readint(fin))
    
    fin.seek(curpos,0)

    return uelist

pduTranslist = ['CQI', 'SR', 'HARQ', 'SR_HARQ', 'CQI_HARQ', 'CQI_SR', 'CQI_SR_HARQ']
def pucch_log(logFilePath):
    flag = True
    inFilepath = os.path.join(logFilePath,'gPhyCatchDataBuf.bin')
    outFilepath = os.path.join(logFilePath,'pucchLog.csv')
    print(inFilepath)
    with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(["numant","frame_structure","sf_idx","ul_dl_config","n_cell_id","inv_q","fft_size","bw","mode","num_rb","num_user",  "pdu_type", "shorten:4",  "num_sr_idx: 4", "m_sr", "ridx_sr", "num_an", "an_mode:4", "num_an_idx:4", "n_rnti", "m_f1[0]", "m_f1[1]", "m_f1[2]", "m_f1[3]", "r_idx_f1[0]", "r_idx_f1[1]", "r_idx_f1[2]", "r_idx_f1[3]", "num_cqi_data",  "num_cqi_idx",   "m_f2", "r_idx_f2","out_ul_cqi", "out_sr",     "out_num_an", "out_mode",   "out_an4:4", "out_an0:4", "out_an5:4",  "out_an1:4",  "out_an6:4",  "out_an2:4",  "out_an7:4",  "out_an3:4",  "out_num_dl_cqi", "out_snr","out_ts","out_data"])
        with open(inFilepath,'rb') as fin:
            
            while flag:
                loglist = []
                loglist.extend(read2_4bit(fin))
                loglist.append(readchar(fin))
                fin.seek(1, 1)#cptype
                loglist.append(readchar(fin))
                
                fin.seek(4, 1)# "rs_group_hop",  "n_cs",  "delta_pucch_shift", "n_rb_2"
                
                loglist.append(readshort(fin))
                loglist.append(readshort(fin))

                loglist.extend(read2_4bit(fin))
                loglist.append(readchar(fin))
                loglist.append(readchar(fin))
                pucchNum = readchar(fin)
                loglist.append(pucchNum)

                for i in range(pucchNum):
                    ueOutlist = readPucchOut(fin, i, pucchNum)
                    uelist = []
                    pdutype = readchar(fin)
                    pdutypeStr = pduTranslist[pdutype]
                    uelist.append(pdutypeStr)
                    uelist.extend(read2_4bit(fin))
                    uelist.append(readchar(fin))
                    fin.seek(1, 1)

                    uelist.append(readshort(fin))
                    fin.seek(2, 1)
                    
                    uelist.append(readchar(fin))
                    uelist.extend(read2_4bit(fin))
                    uelist.append(readshort(fin))

                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))

                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))

                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    fin.seek(1, 1)

                    uelist.append(readshort(fin))
                    fin.seek(2, 1)
                    
                    csv_writer.writerow(loglist + uelist + ueOutlist)
                
                if readchar(fin) == 0x5a:
                    print("PUCCH LOG END！")
                    break
                fin.seek(-1, 1)

        fin.close()
    fout.close()

def pusch_log(logFilePath):
    flag = True
    inFilepath = os.path.join(logFilePath,'gPhyCatchDataBuf.bin')
    outFilepath = os.path.join(logFilePath,'puschLog.csv')
    with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(["i_sf_num",   "i_cell_id",  "i_num_User", "ul_harq_history_dur", "i_starting_rb1", "i_starting_rb2", "i_num_rb", "num_tb:4", "i_shorten:4",  "i_ndi_1:4", "i_ndi:4", "i_harq_index_1:4",   "i_harq_index:4", "i_mod_1:4",   "i_mod:4", "i_tdd_bund",    "i_num_codeblock",         "i_rv_1:4",  "i_rv:4",   "i_num_an_bits", "i_codeword_index_1:4",    "i_codeword_index:4",      "i_an_seq", "i_freq_hop",  "i_tbs", "i_k_plus",  "i_num_code_sym_ack", "i_num_code_sym_ri",  "i_num_code_sym_cqi0",  "i_num_code_sym_cqi1",  "i_nrnti",  "num_layer:4",  "num_carrier:4",  "i_cqi_offsert",   "m_sc_pusch_initial", "i_tbs_1", "n_sym_pusch_initial",     "ri_bits[0]",   "num_cqi_bit_carrier[0][0]", "num_cqi_bit_carrier[0][1]", "tb_crc", "cb0_x_crc", "ack_d", "ack_val", "cqi_amount", "ri_val"])
        with open(inFilepath,'rb') as fin:
            
            while flag:
                fin.seek(3, 1)
                loglist = []
                loglist.append(readchar(fin))
                loglist.append(readshort(fin))
                puschUEnum = readchar(fin)
                loglist.append(puschUEnum)
                loglist.append(readchar(fin))

                for i in range(puschUEnum):
                    ueOutlist = readPuschOutAll(fin, i, puschUEnum)
                    
                    uelist = []
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.extend(read2_4bit(fin))

                    uelist.extend(read2_4bit(fin))
                    uelist.extend(read2_4bit(fin))
                    uelist.extend(read2_4bit(fin))
                    uelist.append(readchar(fin))

                    uelist.append(readchar(fin))
                    uelist.extend(read2_4bit(fin))
                    uelist.append(readchar(fin))
                    uelist.extend(read2_4bit(fin))

                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readshort(fin))

                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))

                    uelist.extend(read2_4bit(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readshort(fin))
                    
                    uelist.append(readshort(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))#ri[0]
                    fin.seek(4, 1)

                    uelist.append(readshort(fin))#cqi[0][0]
                    uelist.append(readshort(fin))#cqi[0][1]
                    fin.seek(76, 1)
                    
                    csv_writer.writerow(loglist + uelist + ueOutlist)

                fin.seek(puschUEnum*20, 1)

                if readchar(fin) == 0x5a:
                    print("PUSCH LOG END！")
                    break
                fin.seek(-1, 1)

        fin.close()
    fout.close()

def dlCtrl_log(logFilePath):
    flag = True
    inFilepath = os.path.join(logFilePath,'gPhyCatchDataBuf.bin')
    outFilepath = os.path.join(logFilePath,'dlCTRL_log.csv')
    with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(["rs_power",     "n_cfi",        "pcfich_gain",  "in_pbch_pdu",  "pbch_gain",    "pdcch_gain",   "n_pdcch_pdu",  "n_phich_pdu",  "phich_gain",   "n_sf",         "ret",          "pdcch-dataPayload",        "pdcch-len",          "pdcch-cce_idx",      "pdcch-rnti",         "pdcch-ue_tx_ant",    "pdcch-agg_level",    "pdcch-zero_padding", "phich-rb_start",     "phich-n_dmrs",       "phich-val",          "phich-i_phich",      "phich-gain",         "phich-zero_padding"])
        with open(inFilepath,'rb') as fin:
            
            while flag:
                loglist = []
                loglist.append(readchar(fin))
                loglist.append(readchar(fin))
                loglist.append(readshort(fin))
                loglist.append(readint(fin))
                loglist.append(readshort(fin))
                loglist.append(readshort(fin))
                pdcchNum = readchar(fin)
                loglist.append(pdcchNum)
                phichNum = readchar(fin)
                loglist.append(phichNum)
                loglist.append(readshort(fin))
                loglist.append(readshort(fin))
                loglist.append(readshort(fin))

                for i in range(pdcchNum):
                    payload1,payload2 = readDCIpayload(fin, i, pdcchNum)
                    payloadall = str(payload1)+str(payload2)
                    uelist = []
                    uelist.append(readint(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readshort(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readshort(fin))
                    uelist[0] = payloadall
                    
                    csv_writer.writerow(loglist + uelist)
                fin.seek(pdcchNum*8, 1)

                for i in range(phichNum):
                    templist = ["--","--","--","--","--","--","--"]
                    uelist = []
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readshort(fin))
                    uelist.append(readshort(fin))

                    csv_writer.writerow(loglist + templist + uelist)
                
                if readchar(fin) == 0x5a:
                    print("DL CTRL LOG END！")
                    break
                fin.seek(-1, 1)

        fin.close()
    fout.close()

def pdsch_log(logFilePath):
    flag = True
    inFilepath = os.path.join(logFilePath,'gPhyCatchDataBuf.bin')
    outFilepath = os.path.join(logFilePath,'pdschLog.csv')
    with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(["n_cfi","n_pdu","n_rf","n_sf","rs_gain","pss_gain", "sss_gain","prs_gain","prs_enable","mbsfn_en","csi_gain", "csi_enable","rnti","resrc_alloc_type", "vrb_assign_flag",  "rb_coding",  "mod",  "redundancy_ver", "pdsch_start","tb_idx","tb_swap",  "tx_sch", "n_layers",  "n_subbands","ue_category", "p_a",  "delta_pwr_offset_idx","n_gap","n_prb","tx_mode","codebook_idx[0]","tb_size", "*inptr_tb_data","n_SCID", "ue_rs_antenna_port_index"])
        with open(inFilepath,'rb') as fin:
            
            while flag:
                loglist = []
                loglist.append(readchar(fin))
                pdschUEnum = readchar(fin)
                loglist.append(pdschUEnum)
                loglist.extend(read2_4bit(fin))
                loglist.append(readchar(fin))
                
                loglist.append(readshort(fin))
                loglist.append(readshort(fin))

                loglist.append(readshort(fin))
                loglist.append(readchar(fin))
                loglist.append(readchar(fin))

                loglist.append(readshort(fin))
                loglist.append(readchar(fin))

                #CSI_RS
                fin.seek(9, 1)

                for i in range(pdschUEnum):
                    uelist = []
                    uelist.append(readshort(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readint(fin))

                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.extend(read2_4bit(fin))
                    uelist.append(readchar(fin))

                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    #codebook
                    uelist.append(readchar(fin))
                    fin.seek(12, 1)

                    uelist.append(readshort(fin))
                    uelist.append(readint(fin))

                    fin.seek(10, 1)
                    uelist.append(readchar(fin))
                    uelist.append(readchar(fin))
                    
                    csv_writer.writerow(loglist + uelist)

                if readchar(fin) == 0x5a:
                    print("PDSCH LOG END！")
                    break
                fin.seek(-1, 1)

        fin.close()
    fout.close()


def readrecoder(fin):
    rsltlist = []
    data = fin.read(4)
    outdata = struct.unpack('>I', data)
    total = int(outdata[0])
    rsltlist.append(total & 0xf)#event
    rsltlist.append((total >> 4) & 0xf)#number_of_jobs_undone
    rsltlist.append((total >> 8) & 0xf)#sf
    rsltlist.append((total >> 12) & 0xf)#num_symbols
    rsltlist.append((total >> 16) & 0x0ffff)#idx

    return rsltlist

def pdschedf_debug(logFilePath):
    PDSCHEDF_RECORD_SIZE = 200
    flag = True
    inFilepath = os.path.join(logFilePath,'g_pdschedf_debug.bin')
    # outFilepath = os.path.join(logFilePath,'g_pdschedf_debug.csv')
    # with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
    #     csv_writer = csv.writer(fout)
    #     csv_writer.writerow(["event","number_of_jobs_undone","sf","num_symbols","idx", "timestamp"])
    alllist = []
    columns = ["event","number_of_jobs_undone","sf","num_symbols","idx", "timestamp"]
    with open(inFilepath,'rb') as fin:
        
        while flag:            
            
            record_list = []
            timestamp_list = []

            for i in range(PDSCHEDF_RECORD_SIZE):
                record = readrecoder(fin)
                record_list.append(record)
                pass

            for i in range(PDSCHEDF_RECORD_SIZE):                    
                timestamp_list.append(readint(fin))
                pass


            for i in range(PDSCHEDF_RECORD_SIZE):
                loglist = []
                record = record_list[i]
                
                loglist = record
                loglist.append(timestamp_list[i])
                alllist.append(loglist)
                # csv_writer.writerow(loglist)
                pass

            flag = False
            pass

    fin.close()
    return columns,alllist
    # fout.close()

def pufft_debug(logFilePath):
    PDSCHEDF_RECORD_SIZE = 200
    flag = True
    inFilepath = os.path.join(logFilePath,'g_rxfft_debug.bin')
    # outFilepath = os.path.join(logFilePath,'g_rxfft_debug.csv')
    # with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
    #     csv_writer = csv.writer(fout)
    #     csv_writer.writerow(["event","dispatched_but_not_finished","sf","num_symbols","idx", "timestamp"])
    columns = ["event","dispatched_but_not_finished","sf","num_symbols","idx", "timestamp"]
    alllist = []
    with open(inFilepath,'rb') as fin:
        
        while flag:
            
            record_list = []
            timestamp_list = []

            for i in range(PDSCHEDF_RECORD_SIZE):
                record = readrecoder(fin)
                record_list.append(record)
                pass

            for i in range(PDSCHEDF_RECORD_SIZE):                    
                timestamp_list.append(readint(fin))
                pass


            for i in range(PDSCHEDF_RECORD_SIZE):
                loglist = []
                record = record_list[i]
                
                loglist = record
                loglist.append(timestamp_list[i])
                # csv_writer.writerow(loglist)
                alllist.append(loglist)
                pass             

            flag = False
            pass

    fin.close()
    # fout.close()
    return columns,alllist
	
def eftpe_debug(logFilePath):
    PDSCHEDF_RECORD_SIZE = 200
    flag = True
    inFilepath = os.path.join(logFilePath,'g_eftpe_debug.bin')
    outFilepath = os.path.join(logFilePath,'g_eftpe_debug.csv')
    with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(["event","readPtr/antid","wirterPtr/pmid","numUser/type","idx", "timestamp"])
        with open(inFilepath,'rb') as fin:
            
            while flag:
                
                record_list = []
                timestamp_list = []

                for i in range(PDSCHEDF_RECORD_SIZE):
                    record = readrecoder(fin)
                    record_list.append(record)
                    pass

                for i in range(PDSCHEDF_RECORD_SIZE):                    
                    timestamp_list.append(readint(fin))
                    pass


                for i in range(PDSCHEDF_RECORD_SIZE):
                    loglist = []
                    record = record_list[i]
                    
                    loglist = record
                    loglist.append(timestamp_list[i])
                    csv_writer.writerow(loglist)
                    pass             

                flag = False
                pass

        fin.close()
    fout.close()

def puschEdf_debug(logFilePath):
    PDSCHEDF_RECORD_SIZE = 200
    flag = True
    inFilepath = os.path.join(logFilePath,'g_puschedf_debug.bin')
    outFilepath = os.path.join(logFilePath,'g_puschedf_debug.csv')
    with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(["event","rsv","sfi","numUser","idx", "timestamp"])
        with open(inFilepath,'rb') as fin:
            
            while flag:
                
                record_list = []
                timestamp_list = []

                for i in range(PDSCHEDF_RECORD_SIZE):
                    record = readrecoder(fin)
                    record_list.append(record)
                    pass

                for i in range(PDSCHEDF_RECORD_SIZE):                    
                    timestamp_list.append(readint(fin))
                    pass


                for i in range(PDSCHEDF_RECORD_SIZE):
                    loglist = []
                    record = record_list[i]
                    
                    loglist = record
                    loglist.append(timestamp_list[i])
                    csv_writer.writerow(loglist)
                    pass             

                flag = False
                pass

        fin.close()
    fout.close()	

def cpri_debug(logFilePath):
    PDSCHEDF_RECORD_SIZE = 200
    flag = True
    inFilepath = os.path.join(logFilePath,'g_cpri_debug.bin')
    outFilepath = os.path.join(logFilePath,'g_cpri_debug.csv')
    with open(outFilepath,'w',newline='',encoding='utf-8-sig') as fout:
        csv_writer = csv.writer(fout)
        csv_writer.writerow(["event","rsv","sf","num_symbols","idx", "timestamp"])
        with open(inFilepath,'rb') as fin:
            
            while flag:                
                record_list = []
                timestamp_list = []

                for i in range(PDSCHEDF_RECORD_SIZE):
                    record = readrecoder(fin)
                    record_list.append(record)
                    pass

                for i in range(PDSCHEDF_RECORD_SIZE):                    
                    timestamp_list.append(readint(fin))
                    pass


                for i in range(PDSCHEDF_RECORD_SIZE):
                    loglist = []
                    record = record_list[i]                    
                    loglist = record
                    loglist.append(timestamp_list[i])
                    csv_writer.writerow(loglist)
                    pass 
                flag = False
                pass

        fin.close()
    fout.close()

def cpri_overTimeCnt(logFilePath):
    inFilepath = os.path.join(logFilePath,'g_cpriDebugOutTime.bin')
    outFilepath = os.path.join(logFilePath,'g_cpriDebugOutTime.txt')
    with open(outFilepath,'w') as fileOut:
        with open(inFilepath,'rb') as fin:
            fin.seek(-4, 2)
            numOverTime = int(readint(fin),16)
            strOut = 'ipiTrigCnt         = ' + str(numOverTime) + '\n'
            fileOut.write(strOut)
            fin.seek(0, 0)
            for i in range(numOverTime):
                timeStamp = int(readint(fin),16)
                strOut = 'ipiOutTimestamp[' + str(i) + '] = ' + str(timeStamp) + '\n'
                fileOut.write(strOut)
        fin.close()
    fileOut.close()
    
if __name__ == '__main__':
    pyFilePath = os.getcwd()
    
    cpri_overTimeCnt(pyFilePath)
