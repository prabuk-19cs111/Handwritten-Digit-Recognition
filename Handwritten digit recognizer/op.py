from mnist import MNIST

mndata = MNIST('samples')

images, labels = mndata.load_training()

images, labels = mndata.load_testing()