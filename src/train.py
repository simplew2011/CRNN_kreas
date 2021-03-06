from utils import fake_ctc_loss
import keras
import os
import cv2
import time
from data_generator import DataGenerator
import keras.backend.tensorflow_backend as KTF
import tensorflow as tf
import os


def train_model(model, img_data_dir, train_txt, test_txt, weight_save_path, img_size=(128,32), batch_size=128, max_label_length=12, down_sample_factor=4, epochs=100):
    print("Training start!")

    # train_data_dir, train_data_txt = train_data
    # val_data_dir, val_data_txt = val_data




    # os.environ["CUDA_VISIBLE_DEVICES"] = "0"

    # config = tf.ConfigProto()
    # config.gpu_options.allow_growth=True   #不全部占满显存, 按需分配
    # sess = tf.Session(config=config)

    # KTF.set_session(sess)


    #callbacks  
    save_weights_cbk = keras.callbacks.ModelCheckpoint(weight_save_path, save_best_only=True, save_weights_only=True)
    early_stop_cbk = keras.callbacks.EarlyStopping(patience=3)
    reduce_lr_cbk = keras.callbacks.ReduceLROnPlateau(patience=3)
    
    # compile
    model.compile(optimizer='adam', loss={'ctc_loss_output': fake_ctc_loss})
    # fit_generator
    train_gen = DataGenerator(img_data_dir, train_txt, img_size, down_sample_factor, batch_size, max_label_length)
    val_gen = DataGenerator(img_data_dir, test_txt, img_size, down_sample_factor, batch_size, max_label_length)
    model.fit_generator(generator=train_gen.get_data(),
                        steps_per_epoch=train_gen.img_number//batch_size,
                        validation_data=val_gen.get_data(),
                        validation_steps=val_gen.img_number//batch_size,
                        callbacks=[save_weights_cbk, early_stop_cbk, reduce_lr_cbk], 
                        epochs = epochs)
    print("Training finished!")
    return 0



# def train_model_by_filename(model, train_data_dir, val_data_dir, weight_save_path, img_size=(128,32), batch_size=128, max_label_length=12, down_sample_factor=4, epochs=100):
#     print("Training start!")

#     #callbacks  
#     save_weights_cbk = keras.callbacks.ModelCheckpoint(weight_save_path, save_best_only=True, save_weights_only=True)
#     early_stop_cbk = keras.callbacks.EarlyStopping(patience=10)
#     reduce_lr_cbk = keras.callbacks.ReduceLROnPlateau(patience=5)
    
#     # compile
#     model.compile(optimizer='adam', loss={'ctc_loss_output': fake_ctc_loss})
#     # fit_generator
#     train_gen = DataGenerator(train_data_dir, img_size, down_sample_factor, batch_size, max_label_length)
#     val_gen = DataGenerator(val_data_dir, img_size, down_sample_factor, batch_size, max_label_length)
#     model.fit_generator(generator=train_gen.get_data(),
#                         steps_per_epoch=train_gen.img_number//batch_size,
#                         validation_data=val_gen.get_data(),
#                         validation_steps=val_gen.img_number//batch_size,
#                         callbacks=[save_weights_cbk, early_stop_cbk, reduce_lr_cbk], 
#                         epochs = epochs)
#     print("Training finished!")
#     return 0

def main():

    return 0

if __name__ == "__main__":
    main()
