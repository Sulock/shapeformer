uea_dataset_30 = [
    'ArticularyWordRecognition',
    'AtrialFibrillation',
    'BasicMotions',
    'CharacterTrajectories',
    'Cricket',
    'DuckDuckGeese',
    'ERing',
    'EigenWorms',
    'Epilepsy',
    'EthanolConcentration',
    'FaceDetection',
    'FingerMovements',
    'HandMovementDirection',
    'Handwriting',
    'Heartbeat',
    'InsectWingbeat',
    'JapaneseVowels',
    'LSST',
    'Libras',
    'MotorImagery',
    'NATOPS',
    'PEMS-SF',
    'PenDigits',
    'PhonemeSpectra',
    'RacketSports',
    'SelfRegulationSCP1',
    'SelfRegulationSCP2',
    'SpokenArabicDigits',
    'StandWalkJump',
    'UWaveGestureLibrary'
]

window_size = [
    '50',  # AWR
    '100',  # AF
    '100',  # BM
    '50',   # CT
    '200',
    '10',   # DD
    '50',   # ER
    '10',
    '20',
    '200',
    '10',
    '20',
    '200',
    '20',
    '200',  # Hb
    '10',
    '10',
    '20',
    '10',
    '100',
    '20',
    '50',
    '4',
    '20',
    '10',
    '100',
    '100',
    '10',
    '10',
    '10'
]

shapelets_number = [
    '10',
    '3',
    '10',
    '3',
    '30',
    '100',
    '100',
    '10',
    '30',
    '100',
    '10',
    '30',
    '100',
    '30',
    '100',
    '30',
    '1',
    '10',
    '30',
    '30',
    '1',
    '10',
    '10',
    '30',
    '10',
    '100',
    '100',
    '100',
    '100',
    '10'
]


i = 0
for w_size, s_num in zip(window_size, shapelets_number):
    print("i = ", i, "Window size = ", w_size, "Number of shapelets (per class) = ", s_num)

    save_csv_name = 'main_reuslts'

    # with open('/home/ubuntu/xhc_ws/CF/shapeformer/scripts/uea_cls.sh', 'a') as f:
    #     f.write('python main.py --dataset ' + dataset + ' --save_csv_name ' + save_csv_name + ' --gpu 0' + ';\n')

    with open('/home/ubuntu/xhc_ws/CF/shapeformer/scripts/uea_cls.sh', 'a') as f:
        f.write('python main.py --dataset_pos ' + str(i) +
                ' --window_size ' + w_size +
                ' --num_shapelet ' + s_num +
                ' --gpu 0' + ';\n')

    i = i + 1



## nohup ./scripts/uea_cls.sh &

# new command
# nohup bash ./scripts/uea_cls.sh > uea_train.log 2>&1 &
# jobs -l
