from KGAT_VAE_model.KGAT_VAE import KGAT_VAE_model
from KGAT_VAE_model.KGAT_VAE_Trainer import Trainer
import torch

class KGAT_VAE_Train_Test():
    def __init__(self, args, data, device):
        train_dataloader, test_dataloader, vaild_dataloader, \
        news_title_embedding, entity_adj, relation_adj, entity_dict, kg_env, news_entity_dict, entity_news_dict, user_click_dict, \
        news_title_word_index, news_category_index, news_subcategory_index, category_news_dict, subcategory_news_dict, word_embedding, \
        neibor_embedding, neibor_num, entity_embedding, relation_embedding, ripple_set, \
        vailddata_size, traindata_size, testdata_size, label_test, bound_test = data

        KGAT_VAE = KGAT_VAE_model(args, news_title_embedding, word_embedding, entity_embedding, relation_embedding, news_entity_dict, entity_adj,
                 relation_adj, user_click_dict, news_title_word_index, news_category_index, news_subcategory_index).to(device)
        optimizer_KGAT_VAE = torch.optim.Adam(KGAT_VAE.parameters(), lr = 0.0001)
        self.trainer = Trainer(args, KGAT_VAE, optimizer_KGAT_VAE, data)

    def Train(self):
        print('training begining ...')
        self.trainer.train()

    def Test(self):
        print('testing begining ...')
        self.trainer.test()