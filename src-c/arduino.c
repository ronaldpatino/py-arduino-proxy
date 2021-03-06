#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <inttypes.h>

#include "avr_cpunames.h"

#include "py_arduino_proxy.h"
#include "arduino_type.h"

#define PY_ARDUINO_PROXY_LCD_SUPPORT %(PY_ARDUINO_PROXY_LCD_SUPPORT)d // {***PLACEHOLDER***}
#define PY_ARDUINO_PROXY_DEBUG_TO_LCD %(PY_ARDUINO_PROXY_DEBUG_TO_LCD)d // {***PLACEHOLDER***}

#if PY_ARDUINO_PROXY_LCD_SUPPORT == 1
#include <LiquidCrystal.h>
#endif

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// If PY_ARDUINO_PROXY_DEVEL is defined, the generated code
// is targeted to test and develop the sketch in a PC,
// this means the code won't run on Arduino

#define PY_ARDUINO_PROXY_DEVEL // removed when generating the sketch.

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// MAX_RECEIVED_PARAMETERS: max count of parameter received from Serial.
// The first parameter is the function name to execute.

#define MAX_RECEIVED_PARAMETERS 10

char* received_parameters[MAX_RECEIVED_PARAMETERS] = { 0 };

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Size of temporal array for storing each of the parameters
// received from Serial. This limit the max. length that a
// parameter may have.

#define TEMPORARY_ARRAY_SIZE 24

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Default pin for blinking and for using as 'start'.

#define PIN_ONBOARD_LED 13  // DIGITAL
#define PIN_START_BUTTON 12 // DIGITAL

// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
// Interrupts

#define ATTACH_INTERRUPT_MODE_LOW '%(ATTACH_INTERRUPT_MODE_LOW)s' // {***PLACEHOLDER***}
#define ATTACH_INTERRUPT_MODE_CHANGE '%(ATTACH_INTERRUPT_MODE_CHANGE)s' // {***PLACEHOLDER***}
#define ATTACH_INTERRUPT_MODE_RISING '%(ATTACH_INTERRUPT_MODE_RISING)s' // {***PLACEHOLDER***}
#define ATTACH_INTERRUPT_MODE_FALLING '%(ATTACH_INTERRUPT_MODE_FALLING)s' // {***PLACEHOLDER***}

volatile uint8_t detected_interrupts = 0x00;

void set_mark_interrupt_0() { detected_interrupts = detected_interrupts | 0x01; }
void set_mark_interrupt_1() { detected_interrupts = detected_interrupts | 0x02; }

void clear_mark_interrupt_0() { detected_interrupts = detected_interrupts & (~0x01); }
void clear_mark_interrupt_1() { detected_interrupts = detected_interrupts & (~0x02); }

uint8_t check_mark_interrupt_0() { return detected_interrupts & 0x01; }
uint8_t check_mark_interrupt_1() { return detected_interrupts & 0x02; }

uint8_t debug_enabled = 0;

#if PY_ARDUINO_PROXY_LCD_SUPPORT == 1
LiquidCrystal lcd = LiquidCrystal(PY_ARDUINO_PROXY_LCD_SUPPORT_rs,
	PY_ARDUINO_PROXY_LCD_SUPPORT_enable, PY_ARDUINO_PROXY_LCD_SUPPORT_d4,
	PY_ARDUINO_PROXY_LCD_SUPPORT_d5, PY_ARDUINO_PROXY_LCD_SUPPORT_d6,
	PY_ARDUINO_PROXY_LCD_SUPPORT_d7);
#endif

#ifndef PY_ARDUINO_PROXY_DEVEL
	
	%(proxied_function_source)s // {***PLACEHOLDER***}
	
	// PROXIED_FUNCTION_COUNT: how many proxied functions we have
	#define PROXIED_FUNCTION_COUNT %(proxied_function_count)d // {***PLACEHOLDER***}
	
	proxied_function_ptr function_ptr[PROXIED_FUNCTION_COUNT] = { %(proxied_function_ptrs)s }; // {***PLACEHOLDER***}
	char*               function_name[PROXIED_FUNCTION_COUNT] = { %(proxied_function_names)s }; // {***PLACEHOLDER***}
	
	#define read_char() Serial.read()
	
	void setup_serial() {
		Serial.begin(%(serial_speed)d); // {***PLACEHOLDER***}
	}
	
	void wait_start() {
		digitalWrite(PIN_START_BUTTON, HIGH); // turn on pullup resistors
		int state = HIGH;
		while(digitalRead(PIN_START_BUTTON) == LOW) {
			digitalWrite(PIN_ONBOARD_LED, state); // turn the onboard led ON/OFF
			state = !state;
			delay(100);
		}
		digitalWrite(PIN_ONBOARD_LED, HIGH); // turn the onboard led ON
	}
	
	void send_int_response(int value) {
		Serial.println(value, DEC);
	}
	
	// param_num: which parameter is invalid. Starts with '0'.
	// received_parameters[1] -> '0'
	// received_parameters[2] -> '1'
	// received_parameters[3] -> '2'
	void send_invalid_parameter_response(int param_num) {
		Serial.print("%(INVALID_PARAMETER)s "); // {***PLACEHOLDER***}
		Serial.println(param_num, DEC);
	}
	
	// error_code == 0 -> UNKNOWN ERROR CORE or WITHOUT ERROR CODE
	void send_invalid_cmd_response(int error_code) {
		Serial.print("%(INVALID_CMD)s "); // {***PLACEHOLDER***}
		Serial.println(error_code, DEC);
	}

	// Inform that the command is not supported.
	// This is used in LCD commands, to report that the command existed,
	// but it's unsupported because the sktech was generated with NO
	// support for LCDs.
	void send_unsupported_cmd_response() {
		Serial.print("%(UNSUPPORTED_CMD)s "); // {***PLACEHOLDER***}
		Serial.println(received_parameters[0]); // The command
	}
	
	void send_ok_response() {
		Serial.println("OK");
	}
	
	void send_char_array_response(char* response) {
		Serial.println(response);
	}
	
	void send_debug() {
		if(debug_enabled == 0) return;
		int i;
		for(i=0; i<MAX_RECEIVED_PARAMETERS; i++) {
					Serial.print("> received_parameters[");
					Serial.print(i);
					Serial.print("] -> ");
			if(received_parameters[i] != NULL) {
						Serial.println(received_parameters[i]);
			} else {
						Serial.println("null");
					}
		}
	}
	
#endif

#ifdef PY_ARDUINO_PROXY_DEVEL // Taken from : wiring.h - Partial implementation of the Wiring API for the ATmega8. Part of Arduino - http://www.arduino.cc/

#define HIGH 0x1
#define LOW  0x0

#define INPUT 0x0
#define OUTPUT 0x1

#define true 0x1
#define false 0x0

#define CHANGE 1
#define FALLING 2
#define RISING 3

#define interrupts() sei()
#define noInterrupts() cli()

typedef unsigned int word;

#define bit(b) (1UL << (b))

typedef uint8_t boolean;
typedef uint8_t byte;

void pinMode(uint8_t a, uint8_t b) { }
void digitalWrite(uint8_t a, uint8_t b) { }
int digitalRead(uint8_t a) { return 0; }
int analogRead(uint8_t a) { return 0; }
void analogReference(uint8_t mode) { }
void analogWrite(uint8_t a, int b) { }

unsigned long millis(void) { return 0; }
unsigned long micros(void) { return 0; }
void delay(unsigned long a) { }
void delayMicroseconds(unsigned int us) { }
unsigned long pulseIn(uint8_t pin, uint8_t state, unsigned long timeout) { return 0; }

void attachInterrupt(uint8_t interruptNum, void (*userFunc)(void), int mode) { }
void detachInterrupt(uint8_t interruptNum) { }

#endif

#ifdef PY_ARDUINO_PROXY_DEVEL
	
	void send_debug() { }
	
	void _ping() {
		printf("ping()\n");
	}
	
	void _analogRead() {
		printf("_analogRead() PIN %s\n", received_parameters[1]);
	}

	// PROXIED_FUNCTION_COUNT: how many proxied functions we have
	#define PROXIED_FUNCTION_COUNT 2

	proxied_function_ptr function_ptr[PROXIED_FUNCTION_COUNT] = { _ping, _analogRead, };
	char* function_name[PROXIED_FUNCTION_COUNT] = { "_ping", "_analogRead", };

	int read_char() {
		char* text = "_ping\n_analogRead 5\n_some_invalid_command\n";
		static int next_return = 0;
		int ret = (int) text[next_return];
		next_return = next_return + 1;
		if(next_return >= strlen(text))
			next_return = 0;
		return ret;
	}
	
	void send_invalid_cmd_response(int error_code) {
		printf("send_invalid_cmd_response(error_code=%d)\n", error_code);
	}
	
	void wait_start() { }
	
	void setup_serial() { }
	
	void send_int_response(int value) { }
	
	void send_invalid_parameter_response() { }
	
	void send_char_array_response(char* response) { }
	
#endif

// Define all the possible return values. This is used as a 'code' for
// reporing errors to python.

#define RETURN_OK												0
#define READ_ONE_PARAM_NEW_LINE_FOUND							7
#define READ_ONE_PARAM_EMPTY_RESPONSE 							1
#define READ_ONE_PARAM_ERROR_PARAMETER_TOO_LARGE 				2
#define READ_PARAMETERS_ERROR_TOO_MANY_PARAMETERS 				3
#define UNEXPECTED_RESPONSE_FROM_READ_ONE_PARAM					4
#define UNEXPECTED_RESPONSE_FROM_READ_PARAMETERS				5
#define FUNCTION_NOT_FOUND										6

extern unsigned int __bss_end;
extern unsigned int __heap_start;
extern void *__brkval;

int freeMemory() {
  int free_memory;

  if((int)__brkval == 0)
     free_memory = ((int)&free_memory) - ((int)&__bss_end);
  else
    free_memory = ((int)&free_memory) - ((int)__brkval);

  return free_memory;
}

//
// Read one parameter from serial and store it in the 'tmp_array'.
//
// Parameters:
// * tmp_array: where to store the chars read from serial.
//
// Returns:
// * RETURN_OK a complete parameter was read.
// * READ_ONE_PARAM_EMPTY_RESPONSE no parameter was read, because
//		nothing was received when read() the serial connection.
// * READ_ONE_PARAM_ERROR_PARAMETER_TOO_LARGE a parameter was read,
//    	but larger than the buffer. (TEMPORARY_ARRAY_SIZE)
//

uint8_t read_one_param(char* tmp_array) {
	
	int incomingByte;
	int pos = 0;
	while (pos < (TEMPORARY_ARRAY_SIZE-1)) {

		incomingByte = read_char();
		if(incomingByte == -1) {
			// no data
			if(pos == 0 && received_parameters[0] == NULL) {
				// return 0 and let Arduino run other tasks
				// instead of waiting with delay().
				return READ_ONE_PARAM_EMPTY_RESPONSE;
			}
			
			// TODO: test this situation, sending 1 character at a time,
			// and waiting between each character sent.
			
			continue;
		}

		// "\t" == 9 -> got a tab
		if(incomingByte == 9) {
			if(pos == 0) {
				// Ignore leading tabs chars
				continue;
			}
			// got a tab! mark end of string and return
			tmp_array[pos] = 0x00;
			return RETURN_OK;
		}
		
		// "\\n" == 10 -> we've reached end of the command
		if(incomingByte == 10) {
			tmp_array[pos] = 0x00; // mark end of string
			return READ_ONE_PARAM_NEW_LINE_FOUND;
		}

		tmp_array[pos++] = incomingByte;

	} // while
	
	// The tmp_array is full. Some character don't fit-in it, and will
	//  be lost!

	// pos == (TEMPORARY_ARRAY_SIZE-1)
	tmp_array[pos] = 0x00; // mark end of string
	
	return READ_ONE_PARAM_ERROR_PARAMETER_TOO_LARGE;
}

//
// Read parameters from serial and store them in received_parameters.
//
// Returns:
// * RETURN_OK all the parameters were read.
// * READ_ONE_PARAM_EMPTY_RESPONSE no parameter was read.
// * READ_ONE_PARAM_ERROR_PARAMETER_TOO_LARGE: a parameter was larger
//			than the permitted. (TEMPORARY_ARRAY_SIZE)
// * READ_PARAMETERS_ERROR_TOO_MANY_PARAMETERS: found more parameters
//			than the permitted. (MAX_RECEIVED_PARAMETERS)
//

uint8_t read_parameters() {
	
	static char tmp_array[TEMPORARY_ARRAY_SIZE];
	
	// Reset 'received_parameters', only if wasn't done earlier...
	if(received_parameters[0] != NULL) {
		int i;
		for(i=0; i<MAX_RECEIVED_PARAMETERS; i++) {
			if(received_parameters[i] != NULL) {
				free(received_parameters[i]); // free
				received_parameters[i] = NULL; // reset
			} else {
				// we can suppose that if this is NULL, the others will
				// be NULL
				break;
			}
		}
	}
	
	int param_index = 0;
	
	for(param_index=0; param_index<MAX_RECEIVED_PARAMETERS;) {
		
		tmp_array[0] = 0x00;
		uint8_t read_status = read_one_param(tmp_array);
		
		if(read_status == RETURN_OK || read_status == READ_ONE_PARAM_NEW_LINE_FOUND) {
			
			if(tmp_array[0] != 0x00) {
				received_parameters[param_index] = (char*) malloc(strlen(tmp_array)+1);
				strcpy(received_parameters[param_index++], &tmp_array[0]);
			}

			if(read_status == RETURN_OK) {
				continue;
			} else {
				return RETURN_OK;
			}
			
			
		} else if(read_status == READ_ONE_PARAM_EMPTY_RESPONSE) {
			if(param_index == 0) {
				// nothing was read, and we are NOT in the middle of a command
				return READ_ONE_PARAM_EMPTY_RESPONSE;
			} else {
				// we are in the middle of something... try again and again...
				continue;
			}
			
		} else if(read_status == READ_ONE_PARAM_ERROR_PARAMETER_TOO_LARGE) {
			// the parameter is larger that the admited.
			while(read_char() != 10); // 10 == '\n'
			return READ_ONE_PARAM_ERROR_PARAMETER_TOO_LARGE;
			
		} else {
			return UNEXPECTED_RESPONSE_FROM_READ_ONE_PARAM;
		}
	}
	
	// Al the 'received_parameters' were used!
	while(read_char() != 10); // 10 == '\n'
	return READ_PARAMETERS_ERROR_TOO_MANY_PARAMETERS;

}

proxied_function_ptr get_function_by_name(char* name) {
	int i;
	for(i=0; i<PROXIED_FUNCTION_COUNT; i++) {
		if(strcmp(name, function_name[i]) == 0) {
			return function_ptr[i];
		}
	}
	return NULL;
}

void loop() {
	uint8_t ret = read_parameters();
	
	#ifdef PY_ARDUINO_PROXY_DEVEL
	printf(" -> read_parameters(): %d\n", ret);
	int i;
	for(i=0; i<MAX_RECEIVED_PARAMETERS; i++) {
		if(received_parameters[i] != NULL) {
			printf(" -> Parametro[%d]: %s\n", i, received_parameters[i]);
		}
	}
	#endif
	
	if(ret == RETURN_OK) {
		send_debug();
		proxied_function_ptr function = get_function_by_name(received_parameters[0]);
		if(function != NULL) {
			#if PY_ARDUINO_PROXY_DEBUG_TO_LCD == 1
			if(debug_enabled == 2) {
				lcd.clear(); // lcd.setCursor(0, 0); // column, line
				lcd.print(received_parameters[0]);
				
				lcd.setCursor(0, 1); // column, line
				int i;
				for(i=1; i<MAX_RECEIVED_PARAMETERS; i++) {
					if(received_parameters[i] != NULL) {
						lcd.print(received_parameters[i]);
						lcd.print(" ");
					}
				}
			}
			#endif
			
			(function)();
			
		} else {
			send_invalid_cmd_response(FUNCTION_NOT_FOUND);
			
			#if PY_ARDUINO_PROXY_DEBUG_TO_LCD == 1
			if(debug_enabled == 2) {
				lcd.clear(); // lcd.setCursor(0, 0); // column, line
				lcd.print(received_parameters[0]);
				lcd.setCursor(0, 1); // column, line
				lcd.print("ERR:invalid cmd");
			}
			#endif
		}
	} else if(ret == READ_ONE_PARAM_EMPTY_RESPONSE) {
		delay(10);
	} else if(ret == READ_ONE_PARAM_ERROR_PARAMETER_TOO_LARGE
		|| ret == READ_PARAMETERS_ERROR_TOO_MANY_PARAMETERS) {
		send_debug();
		send_invalid_cmd_response(ret);
		
		#if PY_ARDUINO_PROXY_DEBUG_TO_LCD == 1
		if(debug_enabled == 2) {
			lcd.clear(); // lcd.setCursor(0, 0); // column, line
			lcd.print(received_parameters[0]);
			lcd.setCursor(0, 1); // column, line
			if(ret == READ_ONE_PARAM_ERROR_PARAMETER_TOO_LARGE)
				lcd.print("ERR:param large");
			else
				lcd.print("ERR:many params");
		}
		#endif
		
	} else {
		send_debug();
		send_invalid_cmd_response(UNEXPECTED_RESPONSE_FROM_READ_PARAMETERS);
		#if PY_ARDUINO_PROXY_DEBUG_TO_LCD == 1
		if(debug_enabled == 2) {
			lcd.clear(); // lcd.setCursor(0, 0); // column, line
			lcd.print(received_parameters[0]);
			lcd.setCursor(0, 1); // column, line
			lcd.print("ERR:unexp resp");
		}
		#endif
	}
}

void setup() {
	// Pin 13 has an LED connected on most Arduino boards.
	pinMode(PIN_ONBOARD_LED, OUTPUT);
	
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	// From Arduino's docs: Arduino (Atmega) pins default to inputs,
	// so they don't need to be explicitly declared as inputs with pinMode(). 
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	// pinMode(PIN_START_BUTTON, INPUT);

	wait_start();

	setup_serial();
	
	#if PY_ARDUINO_PROXY_LCD_SUPPORT == 1
	lcd.begin(PY_ARDUINO_PROXY_LCD_SUPPORT_COLS,
		PY_ARDUINO_PROXY_LCD_SUPPORT_ROWS);
	lcd.clear();
	lcd.print("Py-Arduino-Proxy");
	lcd.setCursor(0, 1); // column, line
	lcd.print("READY!");
	#endif
}

#ifdef PY_ARDUINO_PROXY_DEVEL

int main() {
	setup();
	loop();
	loop();
	loop();
	
	printf("\n");
	printf("detected_interrupts: %d; check_mark_interrupt_0(): %d; check_mark_interrupt_1(): %d\n", detected_interrupts, check_mark_interrupt_0(), check_mark_interrupt_1());
	
	printf("\n");
	set_mark_interrupt_0();
	printf("set_mark_interrupt_0();\n");
	printf("detected_interrupts: %d; check_mark_interrupt_0(): %d; check_mark_interrupt_1(): %d\n", detected_interrupts, check_mark_interrupt_0(), check_mark_interrupt_1());
	
	printf("\n");
	set_mark_interrupt_1();
	printf("set_mark_interrupt_1();\n");
	printf("detected_interrupts: %d; check_mark_interrupt_0(): %d; check_mark_interrupt_1(): %d\n", detected_interrupts, check_mark_interrupt_0(), check_mark_interrupt_1());
	
	printf("\n");
	clear_mark_interrupt_1();
	printf("clear_mark_interrupt_1();\n");
	printf("detected_interrupts: %d; check_mark_interrupt_0(): %d; check_mark_interrupt_1(): %d\n", detected_interrupts, check_mark_interrupt_0(), check_mark_interrupt_1());
	
	printf("\n");
	clear_mark_interrupt_0();
	printf("clear_mark_interrupt_0();\n");
	printf("detected_interrupts: %d; check_mark_interrupt_0(): %d; check_mark_interrupt_1(): %d\n", detected_interrupts, check_mark_interrupt_0(), check_mark_interrupt_1());
	
	return 0;
}

#endif
