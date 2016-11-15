// https://www.interviewbit.com/problems/letter-phone/

#import <Foundation/Foundation.h>

@interface Solution: NSObject
@end

@implementation Solution
    - (NSMutableArray *)arrFromString:(NSString *)letters {
        NSMutableArray *arr = [NSMutableArray new];
        for (int i=0; i < letters.length; i++) {
            NSString *tmp_str = [letters substringWithRange:NSMakeRange(i, 1)];
            [arr addObject:tmp_str];
        }
        return arr;
    }

    -(NSMutableArray *)letterCombinations:(NSMutableString *)A  {
        NSArray *keys = [NSArray arrayWithObjects:@"0", @"1", @"2", @"3", @"4", @"5", @"6", @"7", @"8", @"9", nil];
        NSArray *values = [NSArray arrayWithObjects:@"0", @"1", @"abc", @"def", @"ghi", @"jkl", @"mno", @"pqrs", @"tuv", @"wxyz", nil];
        NSDictionary *dict = [NSDictionary dictionaryWithObjects:values forKeys:keys];
        NSString *c = [A substringWithRange:NSMakeRange(0, 1)];
        NSString *str = [dict objectForKey:c];
        NSMutableArray *strChars = [self arrFromString:str];
        NSMutableString *headlessString = [A mutableCopy];
        // NSLog(@"%@ %@", [headlessString class], @([headlessString respondsToSelector:@selector(deleteCharactersInRange:)]));
        [headlessString deleteCharactersInRange:NSMakeRange(0, 1)];
        if (headlessString.length == 0)
        {
            return strChars;
        }
        NSMutableArray *headlessStringAns = [self letterCombinations:headlessString];
        NSMutableArray *ans = [NSMutableArray array];
        for (NSString *i in strChars)
        {
            for (NSString *j in headlessStringAns)
            {
                NSString *x = [NSString stringWithFormat:@"%@%@", i, j];
                [ans addObject:x];
            }
        }
        return ans;
    }
@end

int main(int argc, char const *argv[])
{
    NSMutableString *a = [@"2" mutableCopy];
    // NSMutableString *a = [NSMutableString new];
    // [a appendString:@"2"];
    Solution *x = [Solution new];
    NSLog(@"%@", [a class]);
    NSLog(@"%@", [x letterCombinations:a]);
    return 0;
}
