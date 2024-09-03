#include <bluetooth/bluetooth.h>
#include <bluetooth/rfcomm.h>
#include <stdio.h>
#include <sys/socket.h>
#include <unistd.h>

int main(int argc, char *[] argv) {
  struct sockaddr_rc addr = {0};
  int s, status, len = 0;
  char dest[18] = "00:12:01:31:01:13";
  char buf[256];

  s = socket(AF_BLUETOOTH, SOCK_STREAM, BTPROTO_RFCOMM);
  addr.rc_family = AF_BLUETOOTH;
  addr.rc_channel = (uint8_t)1;
  str2ba(dest, &addr.rc_bdaddr);

  status = connect(s, (struct sockaddr *)&addr, sizeof(addr));
  if (status) {
    printf(" failed to connect the device!\n");
    return -1;
  }

  do {
    len = read(s, buf, sizeof buf);

    if (len > 0) {
      buf[len] = 0;
      printf("%s\n", buf);
      write(s, buf, strlen(buf));
    }
  } while (len > 0);

  close(s);
  return 0;
}
