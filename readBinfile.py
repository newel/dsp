import struct
import os

phy_debug =[
    ('uint16_t' , 'sfnsf                                    '), 
    ('uint8_t ' , 'phy_dot_info                             '), 
    ('uint8_t ' , 'rsv                                      '), 
    ('uint32_t' , 'phy_indcation[IPC_MESSAGE_CH_ID         ]' ),
    ('uint32_t' , 'phy_indcation[1                         ]' ),
    ('uint32_t' , 'phy_indcation[PARAM_REQUEST_CH_ID       ]' ),
    ('uint32_t' , 'phy_indcation[CONFIG_REQUEST_CH_ID      ]' ),
    ('uint32_t' , 'phy_indcation[START_REQUEST_CH_ID       ]' ),
    ('uint32_t' , 'phy_indcation[STOP_REQUEST_CH_ID        ]' ),
    ('uint32_t' , 'phy_indcation[DL_CONFIG_REQUEST_CH_ID   ]' ),
    ('uint32_t' , 'phy_indcation[UL_CONFIG_REQUEST_CH_ID   ]' ),
    ('uint32_t' , 'phy_indcation[HI_DCI0_REQUEST_CH_ID     ]' ),
    ('uint32_t' , 'phy_indcation[TX_REQUEST_CH_ID          ]' ),
    ('uint32_t' , 'phy_indcation[PARAM_RESPONSE_CH_ID      ]' ),
    ('uint32_t' , 'phy_indcation[CONFIG_RESPONSE_CH_ID     ]' ),
    ('uint32_t' , 'phy_indcation[STOP_INDICATION_CH_ID     ]' ),
    ('uint32_t' , 'phy_indcation[ERROR_INDICATION_CH_ID    ]' ),
    ('uint32_t' , 'phy_indcation[SUBFRAME_INDICATION_CH_ID ]' ),
    ('uint32_t' , 'phy_indcation[HARQ_INDICATION_CH_ID     ]' ),
    ('uint32_t' , 'phy_indcation[CRC_INDICATION_CH_ID      ]' ),
    ('uint32_t' , 'phy_indcation[RX_ULSCH_INDICATION_CH_ID ]' ),
    ('uint32_t' , 'phy_indcation[RACH_INDICATION_CH_ID     ]' ),
    ('uint32_t' , 'phy_indcation[SRS_INDICATION_CH_ID      ]' ),
    ('uint32_t' , 'phy_indcation[RX_SR_INDICATION_CH_ID    ]' ),
    ('uint32_t' , 'phy_indcation[RX_CQI_INDICATION_CH_ID   ]' ),
    ('uint32_t' , 'phy_indcation[DEBUG_CH_ID               ]' ),
    ('uint32_t' , 'osIpcCheckChAvailable_fail               ' )

]
sys_param =[                                               
    ('uint16_t' , 'duplexing_mode                             ' ),
    ('uint16_t' , 'pcfich_power_offset                        ' ),
    ('uint16_t' , 'pb                                         ' ),
    ('uint16_t' , 'dl_cyclic_prefix_type                      ' ),
    ('uint16_t' , 'ul_cyclic_prefix_type                      ' ),
    ('uint16_t' , 'dl_channel_bw                              ' ),
    ('uint16_t' , 'ul_channel_bw                              ' ),
    ('uint16_t' , 'ref_signal_power                           ' ),
    ('uint16_t' , 'tx_antenna_port                            ' ),
    ('uint16_t' , 'rx_antenna_port                            ' ),
    ('uint16_t' , 'phich_resource                             ' ),
    ('uint16_t' , 'phich_duration                             ' ),
    ('uint16_t' , 'phich_power_offset                         ' ),
    ('uint16_t' , 'primary_sync_signal                        ' ),
    ('uint16_t' , 'secondary_sync_signal                      ' ),
    ('uint16_t' , 'physical_cell_id                           ' ),
    ('uint16_t' , 'configuration_index                        ' ),
    ('uint16_t' , 'root_seq_index                             ' ),
    ('uint16_t' , 'zero_corelation_zone_config                ' ),
    ('uint16_t' , 'high_speed_flag                            ' ),
    ('uint16_t' , 'freq_offset                                ' ),
    ('uint16_t' , 'hopping_mode                               ' ),
    ('uint16_t' , 'hopping_offset                             ' ),
    ('uint16_t' , 'num_of_subband                             ' ),
    ('uint16_t' , 'delta_pucch_shift                          ' ),
    ('uint16_t' , 'n_cqi_rb                                   ' ),
    ('uint16_t' , 'n_an_cs                                    ' ),
    ('uint16_t' , 'n1_pucch_an                                ' ),
    ('uint16_t' , 'bandwidth_configuration                    ' ),
    ('uint16_t' , 'mac_up_pts                                 ' ),
    ('uint16_t' , 'srs_subframe_configuration                 ' ),
    ('uint8_t ' , 'srs_ack_nack_simultx                       ' ),
    ('uint8_t ' , 'reserved                                   ' ),
    ('uint16_t' , 'uplink_rs_hopping                          ' ),
    ('uint16_t' , 'group_assignment                           ' ),
    ('uint16_t' , 'cyclic_shift1_for_dmrs                     ' ),
    ('uint16_t' , 'subframe_assignment                        ' ),
    ('uint16_t' , 'special_subframe_patterns                  ' ),
    ('uint16_t' , 'dci_pow_offset                             ' ),
    ('uint16_t' , 'data_reporting_mode                        ' ),
    ('uint16_t' , 'sfn_sf                                     ' ),
    ('uint16_t' , 'phy_state                                  ' ),
    ('uint16_t' , 'dl_bandwidth_support                       ' ),
    ('uint16_t' , 'ul_bandwidth_support                       ' ),
    ('uint16_t' , 'dl_modulation_support                      ' ),
    ('uint16_t' , 'ul_modulation_support                      ' ),
    ('uint16_t' , 'phy_antenna_capability                     ' ),
    ('uint16_t' , 'phy_sync_mode                              ' ),
    ('uint16_t' , 'rach_and_sr_report_mode                    ' ),
    ('uint16_t' , 'srs_configuration_support                  ' ),
    ('uint16_t' , 'phy_version_0                              ' ),
    ('uint16_t' , 'phy_version_1                              ' ),
    ('uint16_t' , 'extraction_window_margin                   ' ),
    ('uint16_t' , 'pucch_noise_estimation_gamma               ' ),
    ('uint16_t' , 'prach_format4_peak_ratio                   ' ),
    ('uint16_t' , 'prach_format0_peak_ratio                   ' ),
    ('uint16_t' , 'doppler_estimation_compensation_factor     ' ),
    ('uint16_t' , 'probability_dtx_ack_pusch                  ' ),
    ('uint16_t' , 'probability_dtx_ack_pucch_Format1          ' ),
    ('uint16_t' , 'per_rb_received_inter_power_est_gamma      ' ),
    ('uint16_t' , 'uplink_payload_allocation_method           ' ),
    ('uint16_t' , 'error_checking_mode                        ' ),
    ('uint16_t' , 'run_time_synchronization_mode              ' ),
    ('uint16_t' , 'pss_tx_antenna_selection                   ' ),
    ('uint16_t' , 'sss_tx_antenna_selection                   ' ),
    ('uint16_t' , 'max_uplink_retx                            ' ),
    ('uint16_t' , 'earfcn                                     ' ),
    ('uint16_t' , 'sniff_earfcn                               ' ),
    ('uint16_t' , 'mrc_irc                                    ' ),
    ('uint16_t' , 'over_exact_sampling                        ' ),
    ('uint16_t' , 'ul_mimo_selection                          ' ),
    ('uint16_t' , 'mbsfn_area_id                              ' ),
    ('uint16_t' , 'prs_bandwidth                              ' ),
    ('uint16_t' , 'prs_cyclic_prefix_type                     ' ),
    ('uint16_t' , 'release_capability                         ' ),
    ('uint16_t' , 'mbsfn_capability                           ' ) 
]
err_log =[
    ('uint32_t' , 'gErrLog[ERRLOG_TTI                         ]' ),
    ('uint32_t' , 'gErrLog[ERRLOG_SLOT0                       ]' ),
    ('uint32_t' , 'gErrLog[ERRLOG_SLOT1                       ]' ),
    ('uint32_t' , 'gErrLog[ERRLOG_AICRXMISS                   ]' ),
    ('uint32_t' , 'gErrLog[ERRLOG_AICTXMISS                   ]' ),
    ('uint32_t' , 'gErrLog[ERRLOG_PRACHMISS                   ]' ),
    ('uint32_t' , 'gErrLog[ERRLOG_SRSMISS                     ]' ),
    ('uint32_t' , 'gErrLog[ERRLOG_PDSCHEDFMISS                ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_SRS_RBERR                   ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_PRACHSTATE_ERR              ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_PRACHFMT_ERR                ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_TxPdu_StartPtr_NULL_PDSCH   ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_TxPdu_StartPtr_NULL_PCH     ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_UL_BW_ERR                   ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_EFTPE_REG_HANDLE_NULL       ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_EFTPE_ADD_HANDLE_NULL       ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_EFTPE_OS_CHDISPATCH_FAIL    ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_EFTPE_ADD_QUENE_FAIL        ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_MAPLE_ERR                   ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_MAPLE_ERRTYPE               ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_L2DataPrefetchERR           ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_PUCCH_MULTPLEX_ANMODE       ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_PUSCH_CfoEst_BWERR          ]' ),
    ('uint32_t' , 'gErrLog[ERRCNT_CPRI_OUT_TIME_ERR           ]' )
]
gEvtMgrCnt =[                                          
    ('uint32_t' , 'gEvtMgrCnt[EVT_DLTTIDELAY       ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_EOS6             ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_EOS10            ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_EOS13            ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_EOPUSCH          ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_EOPDSCHEDF       ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_PRACHCORR        ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_SRSUSERSEP       ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_EOEFTPE          ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_SNIFFSYNC        ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_SNIFFCAPFIN      ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_SN_VITERBI_TURBO ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_SUPFRAME         ]' ),
    ('uint32_t' , 'gEvtMgrCnt[EVT_PRACHRFIN        ]' ),
    ('uint32_t' , 'gEvtMgrCnt[NUMEVT               ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_AICTXSYM        ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_AICRXSYM        ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_SIMRXSYM        ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_DLON            ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_DLOFF           ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_ULON            ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_ULOFF           ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_MBSFNON         ]' ),
    ('uint32_t' , 'gEvtMgrCnt[DEVT_MBSFNOFF        ]' )
]
gEvtWaitCnt =[                                          
    ('uint32_t' , 'gEvtWaitCnt[EVT_DLTTIDELAY       ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_EOS6             ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_EOS10            ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_EOS13            ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_EOPUSCH          ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_EOPDSCHEDF       ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_PRACHCORR        ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_SRSUSERSEP       ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_EOEFTPE          ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_SNIFFSYNC        ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_SNIFFCAPFIN      ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_SN_VITERBI_TURBO ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_SUPFRAME         ]' ),
    ('uint32_t' , 'gEvtWaitCnt[EVT_PRACHRFIN        ]' ),
    ('uint32_t' , 'gEvtWaitCnt[NUMEVT               ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_AICTXSYM        ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_AICRXSYM        ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_SIMRXSYM        ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_DLON            ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_DLOFF           ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_ULON            ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_ULOFF           ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_MBSFNON         ]' ),
    ('uint32_t' , 'gEvtWaitCnt[DEVT_MBSFNOFF        ]' )
]
time_rpt =[
    ('uint32_t' , 'CS_SCHSTART                  '),
    ('uint32_t' , 'CS_SCHEODLCTRLENC_CFG        '),
    ('uint32_t' , 'CS_SCHEOPDSCH_CFG            '),
    ('uint32_t' , 'CS_SCHEOCDMDL                '),
    ('uint32_t' , 'CS_SCHEODLCTRLPREFETCH       '),
    ('uint32_t' , 'CS_SCHEODLCTRLENC1           '),
    ('uint32_t' , 'CS_SCHEOPDSCHEDF1            '),
    ('uint32_t' , 'CS_SCHEODLCTRLENC2           '),
    ('uint32_t' , 'CS_SCHEOPDSCHEDF2            '),
    ('uint32_t' , 'CS_SCHEOCDMUL                '),
    ('uint32_t' , 'CS_SCHEOCDMULCFG             '),
    ('uint32_t' , 'CS_SCHEOMTS6                 '),
    ('uint32_t' , 'CS_SCHEOEOS6                 '),
    ('uint32_t' , 'CS_SCHEORXFFT                '),
    ('uint32_t' , 'CS_SCHEOPUSCHCH1             '),
    ('uint32_t' , 'CS_SCHEOPUCCH1               '),
    ('uint32_t' , 'CS_SCHEOMTS13                '),
    ('uint32_t' , 'CS_SCHEOEOS13                '),
    ('uint32_t' , 'CS_SCHEOPUSCHCH2             '),
    ('uint32_t' , 'CS_SCHEOPUSCHEDF             '),
    ('uint32_t' , 'CS_SCHEOPUCCH2               '),
    ('uint32_t' , 'CS_SCHEOPUSCHEDFWAIT         '),
    ('uint32_t' , 'CS_SCHEOPUSCHCQI             '),
    ('uint32_t' , 'CS_SCHEOCDMOUT               '),
    ('uint32_t' , 'CS_SCHEOMTSEND               '),
    ('uint32_t' , 'CS_PRACHSOFILTER0            '),
    ('uint32_t' , 'CS_PRACHEOFILTER0            '),
    ('uint32_t' , 'CS_PRACHSOFILTER1            '),
    ('uint32_t' , 'CS_PRACHEOFILTER1            '),
    ('uint32_t' , 'CS_PRACHSOFILTER2            '),
    ('uint32_t' , 'CS_PRACHEOFILTER2            '),
    ('uint32_t' , 'CS_PRACHSOFILTER3            '),
    ('uint32_t' , 'CS_PRACHEOFILTER3            '),
    ('uint32_t' , 'CS_PRACHSOFILTER4            '),
    ('uint32_t' , 'CS_PRACHEOFILTER4            '),
    ('uint32_t' , 'CS_PRACHSOFILTER5            '),
    ('uint32_t' , 'CS_PRACHEOFILTER5            '),
    ('uint32_t' , 'CS_PRACHSOFILTER6            '),
    ('uint32_t' , 'CS_PRACHEOFILTER6            '),
    ('uint32_t' , 'CS_PRACHSOFILTER7            '),
    ('uint32_t' , 'CS_PRACHEOFILTER7            '),
    ('uint32_t' , 'CS_PRACHSOFILTER8            '),
    ('uint32_t' , 'CS_PRACHEOFILTER8            '),
    ('uint32_t' , 'CS_PRACHSOFILTER9            '),
    ('uint32_t' , 'CS_PRACHEOFILTER9            '),
    ('uint32_t' , 'CS_PRACHSOFILTER10           '),
    ('uint32_t' , 'CS_PRACHEOFILTER10           '),
    ('uint32_t' , 'CS_PRACHSOFILTER11           '),
    ('uint32_t' , 'CS_PRACHEOFILTER11           '),
    ('uint32_t' , 'CS_PRACHSOCORR0              '),
    ('uint32_t' , 'CS_PRACHEOCORR0              '),
    ('uint32_t' , 'CS_PRACHSOCORR1              '),
    ('uint32_t' , 'CS_PRACHEOCORR1              '),
    ('uint32_t' , 'CS_PRACHSOCORR2              '),
    ('uint32_t' , 'CS_PRACHEOCORR2              '),
    ('uint32_t' , 'CS_PRACHSOCORR1_A2           '),
    ('uint32_t' , 'CS_PRACHEOCORR1_A2           '),
    ('uint32_t' , 'CS_PRACHSOCORR2_A3           '),
    ('uint32_t' , 'CS_PRACHEOCORR2_A3           '),
    ('uint32_t' , 'CS_PRACHSOCORR3              '),
    ('uint32_t' , 'CS_PRACHEOCORR3              '),
    ('uint32_t' , 'CS_PRACHSODEC0               '),
    ('uint32_t' , 'CS_PRACHEODEC0               '),
    ('uint32_t' , 'CS_PRACHSODEC1               '),
    ('uint32_t' , 'CS_PRACHEODEC1               '),
    ('uint32_t' , 'CS_PRACHSODEC2               '),
    ('uint32_t' , 'CS_PRACHEODEC2               '),
    ('uint32_t' , 'CS_PRACHSODEC3               '),
    ('uint32_t' , 'CS_PRACHEODEC3               '),
    ('uint32_t' , 'CS_PRACHSODEC4               '),
    ('uint32_t' , 'CS_PRACHEODEC4               '),
    ('uint32_t' , 'CS_PRACHSODEC5               '),
    ('uint32_t' , 'CS_PRACHEODEC5               '),
    ('uint32_t' , 'CS_SRSSODATASEP              '),
    ('uint32_t' , 'CS_SRSEODATASEP              '),
    ('uint32_t' , 'CS_SRSSOPREMULTA0            '),
    ('uint32_t' , 'CS_SRSEOPREMULTA0            '),
    ('uint32_t' , 'CS_SRSSOIDFTA0               '),
    ('uint32_t' , 'CS_SRSEOIDFTA0               '),
    ('uint32_t' , 'CS_SRSSOPREMULTA1            '),
    ('uint32_t' , 'CS_SRSEOPREMULTA1            '),
    ('uint32_t' , 'CS_SRSSOIDFTA1               '),
    ('uint32_t' , 'CS_SRSEOIDFTA1               '),
    ('uint32_t' , 'CS_SRSSOUSEREXTA0            '),
    ('uint32_t' , 'CS_SRSEOUSEREXTA0            '),
    ('uint32_t' , 'CS_SRSSODFTA0                '),
    ('uint32_t' , 'CS_SRSEODFTA0                '),
    ('uint32_t' , 'CS_SRSSOUSEREXTA1            '),
    ('uint32_t' , 'CS_SRSEOUSEREXTA1            '),
    ('uint32_t' , 'CS_SRSSODFTA1                '),
    ('uint32_t' , 'CS_SRSEODFTA1                '),
    ('uint32_t' , 'CS_SRSSOPREMULTA2            '),
    ('uint32_t' , 'CS_SRSEOPREMULTA2            '),
    ('uint32_t' , 'CS_SRSSOIDFTA2               '),
    ('uint32_t' , 'CS_SRSEOIDFTA2               '),
    ('uint32_t' , 'CS_SRSSOPREMULTA3            '),
    ('uint32_t' , 'CS_SRSEOPREMULTA3            '),
    ('uint32_t' , 'CS_SRSSOIDFTA3               '),
    ('uint32_t' , 'CS_SRSEOIDFTA3               '),
    ('uint32_t' , 'CS_SRSSOUSEREXTA2            '),
    ('uint32_t' , 'CS_SRSEOUSEREXTA2            '),
    ('uint32_t' , 'CS_SRSSODFTA2                '),
    ('uint32_t' , 'CS_SRSEODFTA2                '),
    ('uint32_t' , 'CS_SRSSOUSEREXTA3            '),
    ('uint32_t' , 'CS_SRSEOUSEREXTA3            '),
    ('uint32_t' , 'CS_SRSSODFTA3                '),
    ('uint32_t' , 'CS_SRSEODFTA3                '),
    ('uint32_t' , 'CS_SRSSOSTATUS               '),
    ('uint32_t' , 'CS_SRSEOSTATUS               '),
    ('uint32_t' , 'CS_SRSSOMEAS                 '),
    ('uint32_t' , 'CS_SRSEOMEAS                 ')
]

def ReadFile_debug(binFilePath, fileName):
    columns,alllist = ['key','value'],[]
    path2open = os.path.join(binFilePath,fileName)
    with open(path2open,'rb') as binfile:
        logCnt = 1
        reflist = []
        if 'gPhyDebug' in fileName:
            reflist = phy_debug
        elif 'sys_param' in fileName:
            reflist = sys_param
        elif 'gErrLog' in fileName:
            reflist = err_log
        elif 'gEvtMgrCnt' in fileName:
            reflist = gEvtMgrCnt
        elif 'gEvtWaitCnt' in fileName:
            reflist = gEvtWaitCnt
        elif 'gcsReport' in fileName:
            reflist = time_rpt
            logCnt = 10
        elif 'gcsBuf' in fileName:
            reflist = time_rpt
            logCnt = 10
        else:
            return
        # with open(path2open.replace('.bin', '.txt'),'w') as fileOut:
        for i in range(logCnt * len(reflist)):
            if reflist[i % len(reflist)][0] == 'uint32_t':
                data = binfile.read(4)
                outdata = struct.unpack('>I', data)
            elif reflist[i][0] == 'uint16_t':
                data = binfile.read(2)
                outdata = struct.unpack('>H', data)
            elif reflist[i][0] == 'uint8_t ':
                data = binfile.read(1)
                outdata = struct.unpack('B', data)
            strOut = reflist[i % len(reflist)][1] + ' = ' + str(outdata[0]) + ';\n'
            record = []
            record.append(reflist[i % len(reflist)][1])
            record.append(str(outdata[0]))
            alllist.append(record)

            # print(strOut)
        #         fileOut.write(strOut)
        # fileOut.close()
    binfile.close()
    # print(alllist)
    return columns,alllist
    

if __name__ == '__main__':
    pyFilePath = os.getcwd()
    # print(pyFilePath)
    alllist = ReadFile_debug(pyFilePath, 'sys_param.bin')
    print(alllist)
    
