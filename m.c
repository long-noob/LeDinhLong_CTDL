#include <mega16.h>
#include <delay.h>
#define LED7 PORTC
#define DK7 PORTD
unsigned int MADEM1[10] = {0xC0, 0xF9, 0xA4, 0xB0, 0x99, 0x92, 0x82, 0xF8, 0x80, 0x90};
unsigned j = 0;
unsigned a = 8;

// Declare your global variables here

void main(void)
{
    // Declare your local variables here

    // Input/Output Ports initialization
    // Port A initialization
    // Func7=In Func6=In Func5=In Func4=In Func3=In Func2=In Func1=In Func0=In
    // State7=T State6=T State5=T State4=T State3=T State2=T State1=T State0=T
    PORTA = 0x00;
    DDRA = 0x00;

    // Port B initialization
    // Func7=In Func6=In Func5=In Func4=In Func3=In Func2=In Func1=In Func0=In
    // State7=T State6=T State5=T State4=T State3=T State2=T State1=T State0=T
    PORTB = 0x00;
    DDRB = 0x00;

    // Port C initialization
    // Func7=Out Func6=Out Func5=Out Func4=Out Func3=Out Func2=Out Func1=Out Func0=Out
    // State7=0 State6=0 State5=0 State4=0 State3=0 State2=0 State1=0 State0=0
    PORTC = 0x00;
    DDRC = 0xFF;

    // Port D initialization
    // Func7=Out Func6=Out Func5=Out Func4=Out Func3=Out Func2=Out Func1=Out Func0=Out
    // State7=0 State6=0 State5=0 State4=0 State3=0 State2=0 State1=0 State0=0
    PORTD = 0x00;
    DDRD = 0xFF;

    // Timer/Counter 0 initialization
    // Clock source: System Clock
    // Clock value: Timer 0 Stopped
    // Mode: Normal top=0xFF
    // OC0 output: Disconnected
    TCCR0 = 0x00;
    TCNT0 = 0x00;
    OCR0 = 0x00;

    // Timer/Counter 1 initialization
    // Clock source: System Clock
    // Clock value: Timer1 Stopped
    // Mode: Normal top=0xFFFF
    // OC1A output: Discon.
    // OC1B output: Discon.
    // Noise Canceler: Off
    // Input Capture on Falling Edge
    // Timer1 Overflow Interrupt: Off
    // Input Capture Interrupt: Off
    // Compare A Match Interrupt: Off
    // Compare B Match Interrupt: Off
    TCCR1A = 0x00;
    TCCR1B = 0x00;
    TCNT1H = 0x00;
    TCNT1L = 0x00;
    ICR1H = 0x00;
    ICR1L = 0x00;
    OCR1AH = 0x00;
    OCR1AL = 0x00;
    OCR1BH = 0x00;
    OCR1BL = 0x00;

    // Timer/Counter 2 initialization
    // Clock source: System Clock
    // Clock value: Timer2 Stopped
    // Mode: Normal top=0xFF
    // OC2 output: Disconnected
    ASSR = 0x00;
    TCCR2 = 0x00;
    TCNT2 = 0x00;
    OCR2 = 0x00;

    // External Interrupt(s) initialization
    // INT0: Off
    // INT1: Off
    // INT2: Off
    MCUCR = 0x00;
    MCUCSR = 0x00;

    // Timer(s)/Counter(s) Interrupt(s) initialization
    TIMSK = 0x00;

    // USART initialization
    // USART disabled
    UCSRB = 0x00;

    // Analog Comparator initialization
    // Analog Comparator: Off
    // Analog Comparator Input Capture by Timer/Counter 1: Off
    ACSR = 0x80;
    SFIOR = 0x00;

    // ADC initialization
    // ADC disabled
    ADCSRA = 0x00;

    // SPI initialization
    // SPI disabled
    SPCR = 0x00;

    // TWI initialization
    // TWI disabled
    TWCR = 0x00;

    while (1)
    {
        LED7 = MADEM1[j];
        DK7 = 8;
        if (j < 6)
            // j = chayLed(8,j);
            LED = 0x01;
        delay_ms(100);
        for (i = 0; i < a - 1; i++)
        {
            LED = LED << 1;
            delay_ms(100);
        }

        for (i = 0; i < a - 2; i++)
        {
            LED = LED >> 1;
            delay_ms(100);
        }
        j++;
        DK7 = 0x00;
        if (j == 6)
        {
            break;
        }
    }
}