# check for differences between upstream (Alyssa's main repo) and your own forked version
# writes the git diff to a file called diff.diff.
# looks at each file diff that git raises and appends it to its own block
# ignore if it's a new file (no conflicts will occur)
# if it's an existing file, we need to deal with it.
# for modified files, we create a new copy of the modified file and change its name so git doesn't overwrite it
# with the old ("clean") version from Alyssa's main repo.
# pulls down the code from Alyssa's repo and integrates any new updates.
# you will have clean versions of any modified files in addition to the copies you modified.
# clean up old modified files that match each other
        # use cmp command to check for even single-byte differences between any two files that match a wildcard.