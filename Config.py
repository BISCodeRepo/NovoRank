def read_config(PATH_config_text):

    data_configs = {}

    with open(PATH_config_text, encoding='UTF8') as config_file:
        for line in config_file:
            if line[0] == '#':
                pass
            else:
                if 'precusor_search_ppm' in line:
                    data_configs['PPM'] = float(line.split('=')[1].split('#')[0].strip())
                elif 'elution_time' in line:
                    data_configs['ELUTION_TIME'] = int(line.split('=')[1].split('#')[0].strip())
                elif 'training' in line:
                    if line.split('=')[1].split('#')[0].strip() == 'False' or line.split('=')[1].split('#')[0].strip() == 'false':
                        temp = False
                    else:
                        temp = True
                    data_configs['TRAIN'] = temp
                elif 'save_path' in line:
                    data_configs['SAVE_PATH'] = line.split('=')[1].split('#')[0].strip()
                elif 'cluster_result_path' in line:
                    data_configs['CLUSTER_PATH'] = line.split('=')[1].split('#')[0].strip()
                elif 'denovo_result_csv ' in line:
                    data_configs['DE_NOVO'] = line.split('=')[1].split('#')[0].strip()
                elif 'db_result_csv ' in line:
                    data_configs['DB'] = line.split('=')[1].split('#')[0].strip()
                elif 'mgf_path' in line:
                    data_configs['MGF_PATH'] = line.split('=')[1].split('#')[0].strip()
                elif 'features_csv ' in line:
                    data_configs['RESULT_NAME'] = line.split('=')[1].split('#')[0].strip()
                elif 'pre_trained_model ' in line:
                    data_configs['PRE_TRAINED_MODEL'] = line.split('=')[1].split('#')[0].strip()
                elif 'val_size' in line:
                    data_configs['VAL_SIZE'] = float(line.split('=')[1].split('#')[0].strip())
                elif 'epoch' in line:
                    data_configs['EPOCH'] = int(line.split('=')[1].split('#')[0].strip())
                elif 'batch_size' in line:
                    data_configs['BATCH'] = int(line.split('=')[1].split('#')[0].strip())
                elif 'early_stopping' in line:
                    if line.split('=')[1].split('#')[0].strip() == 'False' or line.split('=')[1].split('#')[0].strip() == 'false':
                        temp = False
                    else:
                        temp = True
                    data_configs['EARLY_STOPPING'] = temp
                elif 'model_save_name' in line:
                    data_configs['MODEL_NAME'] = line.split('=')[1].split('#')[0].strip()
                elif 'result_name' in line:
                    data_configs['FINAL_RESULT'] = line.split('=')[1].split('#')[0].strip()

    return data_configs