#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char tmp[1000000];

ssize_t read(int fd, void *buf, size_t count) {
    if (fd >= 5) {
        int len = syscall(0, fd, tmp, count * 8 / 9);
        int x = 0;
        int l = 0;
        int j = 0;
        for (int i = 0; i < len; ++i) {
            x = (x << 9) | tmp[i];
            l += 9;
            while (l >= 8) {
                int y = x >> (l - 8);
                ((char*)buf)[j++] = y & 0xff;
                x &= (1 << (l - 8)) - 1;
                l -= 8;
            }
        }
        if (l > 0) {
            ((char*)buf)[j++] = (x << (8 - l)) & 0xff;
        }
        return j;
    } else {
        return syscall(0, fd, buf, count);
    }
}


ssize_t write(int fd, const void *buf, size_t count) {
    if (fd >= 5) {
        int x = 0;
        int l = 0;
        int j = 0;
        for (int i = 0; i < count; ++i) {
            x = (x << 8) | ((unsigned char*)buf)[i];
            l += 8;
            while (l >= 9) {
                int y = x >> (l - 9);
                if (y & ~0xff) {
                    syscall(1, 2, "FUCK\n", 5);
                }
                tmp[j++] = y & 0xff;
                x &= (1 << (l - 9)) - 1;
                l -= 9;
            }
        }
        syscall(1, fd, tmp, j);
        return count;
    } else {
        return syscall(1, fd, buf, count);
    }
}
