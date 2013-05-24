The pclinuxos version of the dansguardian rpm has been built with sendmail as a dependancy.
Since we are using postfix this package has been rebuilt fixing the dependancy problem.

Should a newer version need to be built the commands used were:


rpmbuild --recompile dansguardian-2.10.0.3-1pclos2007.src.rpm
#Change to spec folder edit pclinuxos-dansguardian.spec
rpmbuild -ba pclinuxos-dansguardian.spec
