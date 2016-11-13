// https://www.interviewbit.com/problems/nearest-smaller-element/

#import <Foundation/Foundation.h>

@interface Solution: NSObject
@end

// @implementation Solution
//     -(NSMutableArray *) prevSmaller:(NSMutableArray *) A  {
//         NSMutableArray *a = [NSMutableArray new];
//         [a addObject:[NSNumber numberWithInteger:-1]];
//         NSNumber *current_min = [A objectAtIndex:0];
//         for (int j = 1; j < A.count; ++j)
//         {
//             NSNumber *i = [A objectAtIndex:j];
//             if (current_min.integerValue > i.integerValue)
//             {
//                 [a addObject:[NSNumber numberWithInteger:-1]];
//                 current_min = i;
//             }
//             else
//             {
//                 [a addObject:current_min];
//             }
//         }
//         return a;
//     }
// @end

// Time limit exceeded

// @implementation Solution
//     -(NSMutableArray *)prevSmaller:(NSMutableArray *)input  {
//         NSNumber *minus1 = [NSNumber numberWithInteger:-1];
//         // NSMutableArray *ans = [NSMutableArray arrayWithCapacity:input.count];
//         NSMutableArray *ans = [NSMutableArray new];
//         for (int i = 0; i < input.count; ++i)
//         {
//             [ans addObject:minus1];
//             // [ans replaceObjectAtIndex:i withObject:minus1];
//         }
//         for (int i = 0; i < input.count; ++i)
//         {
//             for (int j = (i + 1); j < input.count; ++j)
//             {
//                 if ([[input objectAtIndex:i] integerValue]
//                     < [[input objectAtIndex:j] integerValue]) {
//                     [ans replaceObjectAtIndex:j withObject:[input objectAtIndex:i]];
//                 }
//             }
//         }
//         return ans;
//     }
// @end

@implementation Solution
    -(NSMutableArray *)prevSmaller:(NSMutableArray *)input  {
        NSNumber *minus1 = [NSNumber numberWithInteger:-1];
        NSMutableArray *ans = [NSMutableArray new];
        NSMutableArray *stack = [NSMutableArray new];
        [stack addObject:minus1];
        [stack addObject:[input objectAtIndex:0]];
        [ans addObject:minus1];
        for (int i = 1; i < input.count; ++i)
        {
            NSNumber *current = [input objectAtIndex:i];
            while([[stack objectAtIndex:stack.count-1] integerValue] >= [current integerValue]
                && [[stack objectAtIndex:stack.count-1] integerValue] != -1) {
                [stack removeLastObject];
            }
            NSNumber *top_stack = [stack objectAtIndex:stack.count-1];
            [ans addObject:top_stack];
            [stack addObject: current];
        }
        return ans;
    }
@end

int main(int argc, char const *argv[])
{
    NSMutableArray *a = @[ @34, @35, @27, @42, @5, @28, @39, @20, @28 ];
    Solution *x = [Solution new];
    NSLog(@"%@", [x prevSmaller:a]);
    return 0;
}
