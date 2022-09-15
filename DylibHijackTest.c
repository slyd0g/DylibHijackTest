#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <libproc.h>

__attribute__((constructor))
static void myConstructor(int argc, const char **argv)
{
    // Define variables
    pid_t pid; int ret;
    char pathbuf[PROC_PIDPATHINFO_MAXSIZE];
    FILE* fd = NULL;
    
    // Get PID + full process path
    pid = getpid();
    ret = proc_pidpath(pid, pathbuf, sizeof(pathbuf));
    printf("HIJACK_PATH=%s\n", pathbuf);
    
    exit(0);
}
