x < - c(2, 2, 8, 5, 7, 6, 1, 4)
y < -c(10, 5, 4, 8, 5, 4, 2, 9)

df < - cbind(x, y)
df < - as.data.frame(df)
df < -`colnames < -`(df, c('X', 'Y'))
df < -`row.names < -`(df, c('A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'))

xc < - c(7, 7, 3)
yc < - c(8, 3, 3)

centroids < - cbind(xc, yc)
centroids < - as.data.frame(centroids)
centroids < -`colnames < -`(centroids, c('X', 'Y'))
centroids < -`row.names < -`(centroids, c('C1', 'C2', 'C3'))

eucdistcalculator < - function(centroids, df)
{
    numOfRows < - nrow(df)

# create list of x's and y's to be appended as columns to the original df itself
xdist < - NULL
ydist < - NULL
for (i in seq(1:numOfRows)){
xdist < - c(xdist, df[i, 1])
ydist < - c(ydist, df[i, 2])
}
# take distance from each centroid, and append to df as columns
# temp => temporary
eucDist < - NULL
counter < - 1
for (j in seq(1:nrow(centroids))){
    centroid < - as.matrix(centroids[j,])
temp.xdist < - NULL
temp.ydist < - NULL
eucDist < - NULL
# create distance columns
for (k in seq(1:numOfRows)){
temp.xdist < - c( temp.xdist, (xdist[k] - centroid[1]) ** 2 )
temp.ydist < - c( temp.ydist, (ydist[k] - centroid[2]) ** 2 )
eucDist < - c(eucDist, sqrt(temp.xdist[k]+temp.ydist[k]))
}
# rename colums
apendix < - cbind(temp.xdist, temp.ydist, eucDist)
newcolnames < -c( paste('X vs X_C', counter, sep =''), paste('Y vs Y_C', counter, sep =''), paste('Euc. Dist. for C', counter, sep = ''))
apendix < -`colnames < -`(apendix, newcolnames)
# append distance columns
df < - cbind(df, apendix)
counter = counter +1

}
return (df)
}


func1 < - function(a, b)
{'asdf'}

debug(eucdistcalculator)
print('test')
w < - eucdistcalculator(centroids, df)

eucdistcalculatormk2 < - function(centroids, df)
{
numOfRows < - nrow(df)

# create list of x's and y's to be appended as columns to the original df itself
xdist < - NULL
ydist < - NULL
apendix < - NULL
for (i in seq(1:numOfRows)){
xdist < - c(xdist, df[i, 1])
ydist < - c(ydist, df[i, 2])
}
# take distance from each centroid, and append to df as columns
# temp => temporary
eucDist < - NULL
counter < - 1
for (j in seq(1:nrow(centroids))){
centroid < - as.matrix(centroids[j, ])
temp.xdist < - NULL
temp.ydist < - NULL
eucDist < - NULL
# create distance columns
for (k in seq(1:numOfRows)){
    temp.xdist < - c(temp.xdist, (xdist[k] - centroid[1]) ** 2)
temp.ydist < - c(temp.ydist, (ydist[k] - centroid[2]) ** 2)
eucDist < - c(eucDist, sqrt(temp.xdist[k] + temp.ydist[k]))
}
# rename colums
eucDist < - as.matrix(eucDist)
newcolnames < -c(paste('C', counter, sep=''))
eucDist < -`colnames < -`(eucDist, newcolnames)
apendix < - cbind(apendix, eucDist)
counter = counter + 1
}


# add label columns
label < - NULL
for (rownum in seq(1:nrow(df))){
currentrow < - apendix[rownum, ]
smallestDistance < - min(currentrow)
breakout < - 0
for (colnum in seq(1:ncol(apendix))){
if (currentrow[[colnum]] == smallestDistance)
{
    labels < - colnames(apendix)
label < - c(label, labels[colnum])
breakout < - breakout + 1
}
if (breakout > 1){
label < - label[-length(label)]
}
}
}
# append distance columns
df < - cbind(df, apendix)
df < - cbind(df, label)
return (df)
}

debug(eucdistcalculatormk2)
w < -eucdistcalculatormk2(centroids, df)
x < -eucdistcalculatormk2(centroids, df)

x == w

newcentroids < - function(w)
{

c1 = NULL
xc1 = NULL
yc1 = NULL
for (rownum in seq(1:nrow(w))){
if (w[rownum, ncol(w)] == 'C1') {
xc1 < - c(xc1, w[rownum, 1])
yc1 < - c(yc1, w[rownum, 2])
}
}

xc1 < - mean(xc1)
yc1 < - mean(yc1)
c1 < - cbind(xc1, yc1)

c2 = NULL
xc2 = NULL
yc2 = NULL
for (rownum in seq(1:nrow(w))){
if (w[rownum, ncol(w)] == 'C2') {
xc2 < - c(xc2, w[rownum, 1])
yc2 < - c(yc2, w[rownum, 2])
}
}

xc2 < - mean(xc2)
yc2 < - mean(yc2)
c2 < - cbind(xc2, yc2)

c3 = NULL
xc3 = NULL
yc3 = NULL
for (rownum in seq(1:nrow(w))){
if (w[rownum, ncol(w)] == 'C3') {
xc3 < - c(xc3, w[rownum, 1])
yc3 < - c(yc3, w[rownum, 2])
}
}

xc3 < - mean(xc3)
yc3 < - mean(yc3)
c3 < - cbind(xc3, yc3)

centroids < - rbind(c1, c2, c3)
centroids < - as.data.frame(centroids)
centroids < -`colnames < -`(centroids, c('X', 'Y'))
centroids < -`row.names < -`(centroids, c('C1', 'C2', 'C3'))
return (centroids)
}

debug(newcentroids)

newcentroids(w)

df2 < -eucdistcalculatormk2(centroids, df)

centroids2 < - newcentroids(df2)

df3 < - eucdistcalculatormk2(centroids2, dframe1[, c(-3, -4, -5, -6)])

c3 < - newcentroids(df3)

df4 < - eucdistcalculatormk2(c3, df3[, c(-3, -4, -5, -6)])
df4_2 < - eucdistcalculatormk2(c3, df3[, c(-3, -4, -5, -6)])

df4 == df4_2

c4 < - newcentroids(df4)

# debug(eucdistcalculatormk2)
df5 < - eucdistcalculatormk2(c4, df4[, c(-3, -4, -5, -6)])

# debug(newcentroids)
c5 < - newcentroids(df5)

# c1
plot(centroids, xlim=c(0, 10), ylim=c(0, 10), main='iter 1')
points(df, pch=13)
grid(lty=6, col="cornsilk2")
text(centroids, labels=row.names(centroids), pos=4)

# c2
plot(centroids2, xlim=c(0, 10), ylim=c(0, 10), main='iter 2')
points(df, pch=13)
grid(lty=6, col="cornsilk2")
text(centroids2, labels=row.names(centroids2), pos=4)

# c3
plot(c3, xlim=c(0, 10), ylim=c(0, 10), main='iter 3')
points(df, pch=13)
grid(lty=6, col="cornsilk2")
text(c3, labels=row.names(c3), pos=4)

# c4
plot(c4, df, xlim=c(0, 10), ylim=c(0, 10), main='iter 4')
points(df, pch=13)
grid(lty=6, col="cornsilk2")
text(c4, labels=row.names(c4), pos=4)

# c5
plot(c5, xlim=c(0, 10), ylim=c(0, 10))
points(df, pch=13)
grid(lty=6, col="cornsilk2")
text(c5, labels=row.names(c5), pos=4)

c5[3,] = c()