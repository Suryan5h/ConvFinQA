

class parameters():

    prog_name = "retriever"

    # set up your own path here
    root_path = "/content/ConvFinQA/"
    output_path = "/content/ConvFinQA/Output/"
    cache_dir = "/content/ConvFinQA/Output/CacheModels"

    # the name of your result folder.
    model_save_name = "retriever-roberta-large-2e-5-new-train"

    # use "train_turn.json", "dev_turn.json", and "test_turn.json"
    train_file = root_path + "data/data/train_turn.json"
    valid_file = root_path + "data/data/dev_turn.json"
    test_file = root_path + "data/data/test_turn_private.json"

    op_list_file = "operation_list.txt"
    const_list_file = "constant_list.txt"

    # model choice: bert, roberta
    pretrained_model = "bert"
    model_size = "bert-base-uncased"

    # pretrained_model = "roberta"
    # model_size = "roberta-large"

    # mode: train or test
    device = "cuda"
    mode = "train"
    resume_model_path = ""

    ### to load the trained model in test time
    # saved_model_path = output_path + \
    #     "retriever-roberta-large-2e-5-new_20220504055555/saved_model/loads/10/model.pt"
    saved_model_path = output_path + "saved_model/"
    build_summary = False

    option = "rand"
    neg_rate = 3
    topn = 5

    sep_attention = True
    layer_norm = True
    num_decoder_layers = 1

    max_seq_length = 512
    max_program_length = 100
    n_best_size = 20
    dropout_rate = 0.1

    batch_size = 4
    batch_size_test = 16
    epoch = 100
    learning_rate = 2e-5

    report = 300
    report_loss = 100

    train_sample_size = 500
    valid_sample_size = 500
    test_sample_size = 500