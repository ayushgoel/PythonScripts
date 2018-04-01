class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = {}
        for i in cpdomains:
            x = i.split()
            c = int(x[0])
            domains = x[1].split('.')
            for j in xrange(len(domains)):
                domain = '.'.join(domains[j:])
                if d.has_key(domain):
                    d[domain] += c
                else:
                    d[domain] = c

        print d
        ans = []
        for k,v in d.iteritems():
            print k,v
            ans += [str(v) + ' ' + k]
        return ans

s = Solution()
print s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])