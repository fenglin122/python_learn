import tensorflow as tf

# x = tf.Variable([1, 2])
# a = tf.constant([3, 3])
# #增加一个减法op
# sub = tf.subtract(x, a)
# #增加一个加法op
# add = tf.add(x, sub)
#
# print(sub)
# init = tf.global_variables_initializer()
#
# with tf.Session() as sess:
#     sess.run(init)
#     print(sess.run(sub))
#     print(sess.run(add))

#创建一个变量初始化为0
state = tf.Variable(0, name='counter')
#创建一个op，作用是使state加1
new_value = tf.add(state, 1)
#赋值op assign(a, b),把b赋值给a
update = tf.assign(state, new_value)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(state))
    for _ in range(5):
        sess.run(update)
        print(sess.run(state))

